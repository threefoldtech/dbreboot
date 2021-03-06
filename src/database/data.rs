use super::*;
use crate::acl::*;
use crate::storage::Storage;
use anyhow::Context as ErrorContext;
use std::collections::HashMap;
use tokio::sync::mpsc;
use tokio::task::spawn_blocking;

//TODO: use generics for both object store type and meta factory type.
#[derive(Clone)]
pub struct BcdbDatabase<S, I>
where
    S: Storage,
    I: Index,
{
    data: S,
    meta: I,
    acl: ACLStorage<S>,
}

impl<S, I> BcdbDatabase<S, I>
where
    S: Storage,
    I: Index + Clone,
{
    pub fn new(data: S, meta: I, acl: ACLStorage<S>) -> Self {
        BcdbDatabase {
            data: data,
            meta: meta,
            acl: acl,
        }
    }

    fn get_permissions(&self, acl: u64, user: u64) -> Result<Permissions> {
        // self.acl.g
        let mut store = self.acl.clone();
        let acl = match store.get(acl as u32)? {
            Some(acl) => acl,
            None => return Ok(Permissions::default()),
        };

        if acl.users.contains(&user) {
            return Ok(acl.perm);
        }

        Ok(Permissions::default())
    }

    fn is_authorized(&self, ctx: &Context, meta: &Meta, perm: Permissions) -> Result<()> {
        match ctx.authorization {
            Authorization::Owner => Ok(()),
            Authorization::User(user) => {
                if let Some(acl) = meta.acl() {
                    let stored = self
                        .get_permissions(acl, user as u64)
                        .context("failed to get assigned permissions")?;

                    if stored.grants(perm) {
                        return Ok(());
                    }
                }

                bail!(Reason::Unauthorized);
            }
            Authorization::Invalid => bail!(Reason::Unauthorized),
        }
    }
}

#[tonic::async_trait]
impl<S, I> Database for BcdbDatabase<S, I>
where
    S: Storage + Send + Sync + 'static,
    I: Index + Clone,
{
    async fn set(
        &mut self,
        ctx: &Context,
        collection: &str,
        data: Vec<u8>,
        tags: HashMap<String, String>,
        acl: Option<u64>,
    ) -> Result<Key> {
        if !ctx.is_owner() {
            bail!(Reason::Unauthorized)
        }

        let mut meta = Meta::try_from(tags)?;
        if let Some(acl) = acl {
            meta = meta.with_acl(acl);
        }

        meta = meta
            .with_collection(collection)
            .with_size(data.len() as u64)
            .with_created(
                std::time::SystemTime::now()
                    .duration_since(std::time::UNIX_EPOCH)
                    .unwrap()
                    .as_secs(),
            );

        let db = self.data.clone();
        let id = spawn_blocking(move || db.set(None, &data).expect("failed to set data"))
            .await
            .context("failed to run blocking task")?;

        self.meta.set(id, meta).await?;

        Ok(id)
    }

    async fn fetch(&mut self, ctx: &Context, key: Key) -> Result<Object> {
        let meta = self.meta.get(key).await?;

        self.is_authorized(&ctx, &meta, "r--".parse().unwrap())?;

        let db = self.data.clone();
        let data = spawn_blocking(move || db.get(key))
            .await
            .context("failed to run blocking task")?
            .context("failed to get data")?;
        if data.is_none() {
            bail!(Reason::NotFound);
        }

        Ok(Object {
            key: key,
            data: Some(data.unwrap()),
            meta: meta,
        })
    }

    async fn get(&mut self, ctx: &Context, key: Key, collection: &str) -> Result<Object> {
        let meta = self.meta.get(key).await?;

        if !meta.is_collection(&collection) {
            bail!(Reason::NotFound);
        }

        self.is_authorized(&ctx, &meta, "r--".parse().unwrap())?;

        let db = self.data.clone();
        let data = spawn_blocking(move || db.get(key))
            .await
            .context("failed to run blocking task")?
            .context("failed to get data")?;
        if data.is_none() {
            bail!(Reason::NotFound);
        }

        Ok(Object {
            key: key,
            data: Some(data.unwrap()),
            meta: meta,
        })
    }

    async fn head(&mut self, ctx: &Context, key: Key, collection: &str) -> Result<Object> {
        let meta = self.meta.get(key).await?;

        if !meta.is_collection(&collection) {
            bail!(Reason::NotFound);
        }

        self.is_authorized(&ctx, &meta, "r--".parse().unwrap())?;

        Ok(Object {
            key: key,
            data: None,
            meta: meta,
        })
    }

    async fn delete(&mut self, ctx: &Context, key: Key, collection: &str) -> Result<()> {
        let meta = self.meta.get(key).await?;

        if !meta.is_collection(&collection) {
            bail!(Reason::NotFound);
        }

        self.is_authorized(&ctx, &meta, "--d".parse().unwrap())?;

        let meta = Meta::default().with_deleted(true);
        self.meta.set(key, meta).await?;

        // TODO: should the data associated with that object also
        // be deleted? changes to metadata can be restored if you
        // replay the transaction log to the point until the object
        // is not deleted.

        let db = self.data.clone();

        spawn_blocking(move || db.delete(key))
            .await
            .context("failed to run blocking task")?
            .context("failed to delete data")?;

        Ok(())
    }

    async fn update(
        &mut self,
        ctx: &Context,
        key: Key,
        collection: &str,
        data: Option<Vec<u8>>,
        tags: HashMap<String, String>,
        acl: Option<u64>,
    ) -> Result<()> {
        let current = self.meta.get(key).await?;

        self.is_authorized(&ctx, &current, "-w-".parse().unwrap())?;

        if !current.is_collection(&collection) {
            bail!(Reason::NotFound);
        }

        let mut meta = Meta::try_from(tags)?;
        if let Some(acl) = acl {
            if !ctx.is_owner() {
                bail!(Reason::Unauthorized);
            }

            meta = meta.with_acl(acl);
        }

        meta = meta.with_updated(
            std::time::SystemTime::now()
                .duration_since(std::time::UNIX_EPOCH)
                .unwrap()
                .as_secs(),
        );

        if let Some(data) = data {
            meta = meta.with_size(data.len() as u64);
            let db = self.data.clone();
            spawn_blocking(move || db.set(Some(key), &data))
                .await
                .context("failed to run blocking task")?
                .context("failed to set data")?;
        }

        self.meta.set(key, meta).await?;

        Ok(())
    }

    async fn list(
        &mut self,
        ctx: &Context,
        tags: HashMap<String, String>,
        collection: Option<&str>,
    ) -> Result<mpsc::Receiver<Result<Key>>> {
        if !ctx.is_owner() {
            bail!(Reason::Unauthorized);
        }

        let mut meta = Meta::new(tags);

        if let Some(collection) = collection {
            meta.insert(TAG_COLLECTION, collection);
        }

        self.meta.find(meta).await
    }

    async fn find(
        &mut self,
        ctx: &Context,
        tags: HashMap<String, String>,
        collection: Option<&str>,
    ) -> Result<mpsc::Receiver<Result<Object>>> {
        if !ctx.is_owner() {
            bail!(Reason::Unauthorized);
        }

        let mut meta = Meta::new(tags);

        if let Some(collection) = collection {
            meta.insert(TAG_COLLECTION, collection);
        }

        let index = self.meta.clone();

        let (mut tx, rx) = mpsc::channel(10);
        tokio::spawn(async move {
            let mut rx = match index.find(meta).await {
                Ok(rx) => rx,
                Err(err) => {
                    tx.send(Err(anyhow!("{}", err))).await.unwrap();
                    return;
                }
            };

            while let Some(id) = rx.recv().await {
                let id = match id {
                    Ok(id) => id,
                    Err(err) => {
                        tx.send(Err(err)).await.unwrap();
                        return;
                    }
                };

                let meta = match index.get(id).await {
                    Ok(meta) => meta,
                    Err(err) => {
                        tx.send(Err(err)).await.unwrap();
                        return;
                    }
                };

                match tx
                    .send(Ok(Object {
                        key: id,
                        meta: meta,
                        data: None,
                    }))
                    .await
                {
                    Ok(_) => {}
                    Err(err) => {
                        debug!("failed to send result, broken stream: {}", err);
                        break;
                    }
                };
            }
        });

        Ok(rx)
    }
}

#[cfg(test)]
pub mod database_tests {

    use super::*;
    use crate::acl::ACL;
    use crate::database::index::memory::MemoryIndex;
    use crate::database::*;
    use crate::storage::memory::MemoryStorage;

    pub fn get_in_memory_db() -> BcdbDatabase<MemoryStorage, MemoryIndex> {
        let data = MemoryStorage::new();
        let acl = MemoryStorage::new();
        let index = MemoryIndex::new();

        BcdbDatabase::new(data, index, ACLStorage::new(acl))
    }

    #[tokio::test]
    async fn database_owner_set() {
        let mut db = get_in_memory_db();

        // default context has no authorization
        let ctx = Context::default();
        let tags = HashMap::default();
        let result = db
            .set(&ctx, "test", "hello world".into(), tags, None)
            .await
            .map_err(|e| Reason::from(&e));

        assert_eq!(result.is_err(), true);
        assert_eq!(result.err(), Some(Reason::Unauthorized));

        let ctx = Context::default().with_auth(Authorization::Owner);
        let mut tags = HashMap::default();
        tags.insert("tag".into(), "value".into());
        let result = db
            .set(&ctx, "test", "hello world".into(), tags, None)
            .await
            .map_err(|e| Reason::from(&e));

        assert_eq!(result.is_ok(), true);
        assert_eq!(result.unwrap(), 0);
    }

    #[tokio::test]
    async fn database_owner_get() {
        let collection = "test";
        let mut db = get_in_memory_db();

        let ctx = Context::default().with_auth(Authorization::Owner);
        let mut tags = HashMap::default();
        tags.insert("tag".into(), "value".into());
        let data: Vec<u8> = "hello world".into();
        let result = db
            .set(&ctx, collection, data.clone(), tags, None)
            .await
            .map_err(|e| Reason::from(&e));

        assert_eq!(result.is_ok(), true);
        let key = result.unwrap();

        let ctx = Context::default(); //no auth (invalid)
        let result = db
            .get(&ctx, key, collection)
            .await
            .map_err(|e| Reason::from(&e));

        assert_eq!(result.is_err(), true);
        assert_eq!(result.err(), Some(Reason::Unauthorized));

        let ctx = Context::default().with_auth(Authorization::User(100)); //some random that
        let result = db
            .get(&ctx, key, collection)
            .await
            .map_err(|e| Reason::from(&e));

        // since no acl associated with this data. we still should got unauthorized
        assert_eq!(result.is_err(), true);
        assert_eq!(result.err(), Some(Reason::Unauthorized));

        let ctx = Context::default().with_auth(Authorization::Owner); //some random that
        let result = db
            .get(&ctx, key, collection)
            .await
            .map_err(|e| Reason::from(&e));

        // owner should pass
        assert_eq!(result.is_ok(), true);
        let obj = result.unwrap();

        assert_eq!(obj.key, key);
        assert_eq!(obj.meta.get("tag").unwrap(), "value");
        assert_eq!(obj.meta.collection().unwrap(), collection);
        assert_eq!(obj.data.unwrap(), data);
    }

    #[tokio::test]
    async fn database_user_get() {
        let collection = "test";
        let mut db = get_in_memory_db();

        let ctx = Context::default().with_auth(Authorization::Owner);
        let mut tags = HashMap::default();
        tags.insert("tag".into(), "value".into());
        let data: Vec<u8> = "hello world".into();
        let acl = ACL {
            perm: "r--".parse().unwrap(),
            users: vec![100],
        };

        let acl_id = db.acl.create(&acl).unwrap();

        let result = db
            .set(&ctx, collection, data.clone(), tags, Some(acl_id as u64))
            .await
            .map_err(|e| Reason::from(&e));

        assert_eq!(result.is_ok(), true);
        let key = result.unwrap();

        let ctx = Context::default(); //no auth (invalid)
        let result = db
            .get(&ctx, key, collection.into())
            .await
            .map_err(|e| Reason::from(&e));

        assert_eq!(result.is_err(), true);
        assert_eq!(result.err(), Some(Reason::Unauthorized));

        let ctx = Context::default().with_auth(Authorization::User(100)); //authorized user
        let result = db
            .get(&ctx, key, collection)
            .await
            .map_err(|e| Reason::from(&e));

        assert_eq!(result.is_ok(), true);
        let obj = result.unwrap();

        assert_eq!(obj.key, key);
        assert_eq!(obj.meta.get("tag").unwrap(), "value");
        assert_eq!(obj.meta.collection().unwrap(), collection);
        assert_eq!(obj.data.unwrap(), data);

        let ctx = Context::default().with_auth(Authorization::User(1000)); //some random that
        let result = db
            .get(&ctx, key, collection)
            .await
            .map_err(|e| Reason::from(&e));

        // since the acl associated with this data does not have this user id. we should got unauthorized
        assert_eq!(result.is_err(), true);
        assert_eq!(result.err(), Some(Reason::Unauthorized));

        let ctx = Context::default().with_auth(Authorization::Owner); //some random that
        let result = db
            .get(&ctx, key, collection)
            .await
            .map_err(|e| Reason::from(&e));

        assert_eq!(result.is_ok(), true);
        let obj = result.unwrap();

        assert_eq!(obj.key, key);
        assert_eq!(obj.meta.get("tag").unwrap(), "value");
        assert_eq!(obj.meta.collection().unwrap(), collection);
        assert_eq!(obj.data.unwrap(), data);
    }

    #[tokio::test]
    async fn database_user_update() {
        let collection = "test";
        let mut db = get_in_memory_db();

        let ctx = Context::default().with_auth(Authorization::Owner);
        let mut tags = HashMap::default();
        tags.insert("tag".into(), "value".into());
        let data: Vec<u8> = "hello world".into();
        let acl = ACL {
            // only read perm
            perm: "r--".parse().unwrap(),
            users: vec![100],
        };

        let acl_id = db.acl.create(&acl).unwrap();

        let result = db
            .set(&ctx, collection, data.clone(), tags, Some(acl_id as u64))
            .await
            .map_err(|e| Reason::from(&e));

        assert_eq!(result.is_ok(), true);
        let key = result.unwrap();

        let ctx = Context::default().with_auth(Authorization::User(100)); //authorized user
        let mut tags = HashMap::default();
        tags.insert("new".into(), "new value".into());
        let result = db
            .update(&ctx, key, collection, None, tags, None)
            .await
            .map_err(|e| Reason::from(&e));

        assert_eq!(result.is_err(), true);
        assert_eq!(result.err(), Some(Reason::Unauthorized));

        let acl = ACL {
            // write only perm
            perm: "-w-".parse().unwrap(),
            users: vec![100],
        };

        db.acl.update(acl_id, &acl).unwrap();

        let ctx = Context::default().with_auth(Authorization::User(100)); //authorized user
        let mut tags = HashMap::default();
        tags.insert("new".into(), "new value".into());
        let result = db
            .update(&ctx, key, collection, None, tags, None)
            .await
            .map_err(|e| Reason::from(&e));

        assert_eq!(result.is_ok(), true);

        // this get operation should fail, even with the same user because the acl doesn't have read access
        let ctx = Context::default().with_auth(Authorization::User(100)); //some random that
        let result = db
            .get(&ctx, key, collection)
            .await
            .map_err(|e| Reason::from(&e));

        // since the acl associated with this data does not have this user id. we should got unauthorized
        assert_eq!(result.is_err(), true);
        assert_eq!(result.err(), Some(Reason::Unauthorized));
    }

    #[tokio::test]
    async fn database_update() {
        let collection = "test";
        let mut db = get_in_memory_db();

        let ctx = Context::default().with_auth(Authorization::Owner);
        let mut tags = HashMap::default();
        tags.insert("tag".into(), "value".into());
        let data: Vec<u8> = "hello world".into();

        let result = db
            .set(&ctx, collection, data.clone(), tags, None)
            .await
            .map_err(|e| Reason::from(&e));

        assert_eq!(result.is_ok(), true);
        let key = result.unwrap();

        let ctx = Context::default().with_auth(Authorization::Owner);
        let mut tags = HashMap::default();
        tags.insert("new".into(), "new value".into());
        // update tags only
        let result = db
            .update(&ctx, key, collection, None, tags, None)
            .await
            .map_err(|e| Reason::from(&e));

        assert_eq!(result.is_ok(), true);
        let ctx = Context::default().with_auth(Authorization::Owner);
        let result = db
            .get(&ctx, key, collection)
            .await
            .map_err(|e| Reason::from(&e));

        assert_eq!(result.is_ok(), true);
        let obj = result.unwrap();

        assert_eq!(obj.key, key);
        assert_eq!(obj.meta.get("tag").unwrap(), "value");
        assert_eq!(obj.meta.get("new").unwrap(), "new value");
        assert_eq!(obj.meta.collection().unwrap(), collection);
        assert_eq!(obj.data.unwrap(), data);

        let ctx = Context::default().with_auth(Authorization::Owner);
        let tags = HashMap::default();
        // update data only
        let data: Vec<u8> = "hello nwe world".into();
        let result = db
            .update(&ctx, key, collection, Some(data.clone()), tags, None)
            .await
            .map_err(|e| Reason::from(&e));

        assert_eq!(result.is_ok(), true);
        let ctx = Context::default().with_auth(Authorization::Owner);
        let result = db
            .get(&ctx, key, collection)
            .await
            .map_err(|e| Reason::from(&e));

        assert_eq!(result.is_ok(), true);
        let obj = result.unwrap();

        assert_eq!(obj.key, key);
        assert_eq!(obj.meta.get("tag").unwrap(), "value");
        assert_eq!(obj.meta.get("new").unwrap(), "new value");
        assert_eq!(obj.meta.collection().unwrap(), collection);
        assert_eq!(obj.data.unwrap(), data);
    }

    #[tokio::test]
    async fn database_insert_perf() {
        let collection = "test";
        let mut db = get_in_memory_db();

        let ctx = Context::default().with_auth(Authorization::Owner);
        let mut tags = HashMap::default();
        tags.insert("tag".into(), "value".into());
        let data: Vec<u8> = "hello world".into();

        let now = std::time::Instant::now();
        for i in 0..10000u32 {
            db.set(&ctx, collection, data.clone(), tags.clone(), None)
                .await
                .expect("failed to do insert");
        }

        let dur = std::time::Instant::now().duration_since(now);
        println!("Duration: {:?}", dur);
    }
}
