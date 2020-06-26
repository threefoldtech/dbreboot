use crate::auth::header;
use crate::bcdb::generated::acl_client::AclClient;
use crate::bcdb::generated::*;
use crate::identity::Identity;
use anyhow::Error;
use hyper::Body;
use serde::{Deserialize, Serialize};
use warp::http::StatusCode;
use warp::reject::Rejection;
use warp::Filter;

type Client = AclClient<tonic::transport::Channel>;

#[derive(Serialize, Deserialize, Debug)]
struct ACLGetResponse {
    perm: String,
    users: Vec<u64>,
}

#[derive(Serialize, Deserialize, Debug)]
struct ACLSetRequest {
    perm: String,
}

#[derive(Serialize, Deserialize, Debug)]
struct ACLCreateRequest {
    perm: String,
    users: Vec<u64>,
}

#[derive(Serialize, Deserialize, Debug)]
struct ACLUsersRequest {
    users: Vec<u64>,
}

fn set_headers<T>(request: &mut tonic::Request<T>, id: Identity) {
    // sign request.
    request.metadata_mut().append(
        "authorization",
        tonic::metadata::AsciiMetadataValue::from_str(header(&id, None).as_ref()).unwrap(),
    );
}

async fn handle_create(
    cl: Client,
    id: Identity,
    body: ACLCreateRequest,
) -> Result<impl warp::Reply, Rejection> {
    let mut cl = cl.clone();

    let request = AclCreateRequest {
        acl: Some(Acl {
            perm: body.perm,
            users: body.users,
        }),
    };

    let mut request = tonic::Request::new(request);
    set_headers(&mut request, id);

    let response = match cl.create(request).await {
        Ok(response) => response,
        Err(status) => return Err(super::status_to_rejection(status)),
    };

    let response = response.into_inner();

    Ok(warp::reply::with_status(
        warp::reply::json(&response.key),
        StatusCode::CREATED,
    ))
}

async fn handle_set(
    cl: Client,
    id: Identity,
    key: u32,
    body: ACLSetRequest,
) -> Result<impl warp::Reply, Rejection> {
    let mut cl = cl.clone();

    let request = AclSetRequest {
        key: key,
        perm: body.perm,
    };

    let mut request = tonic::Request::new(request);
    set_headers(&mut request, id);

    match cl.set(request).await {
        Ok(response) => response,
        Err(status) => return Err(super::status_to_rejection(status)),
    };

    Ok(warp::reply::reply())
}

async fn handle_get(cl: Client, id: Identity, key: u32) -> Result<impl warp::Reply, Rejection> {
    let mut cl = cl.clone();

    let request = AclGetRequest { key: key };

    let mut request = tonic::Request::new(request);
    set_headers(&mut request, id);

    let response = match cl.get(request).await {
        Ok(response) => response,
        Err(status) => return Err(super::status_to_rejection(status)),
    };

    let response = response.into_inner();

    match response.acl {
        Some(acl) => {
            let act_get_response = ACLGetResponse {
                perm: acl.perm,
                users: acl.users,
            };
            Ok(warp::reply::json(&act_get_response))
        }
        None => Err(warp::reject::not_found()),
    }
}

async fn handle_grant(
    cl: Client,
    id: Identity,
    key: u32,
    body: ACLUsersRequest,
) -> Result<impl warp::Reply, Rejection> {
    let mut cl = cl.clone();

    let request = AclUsersRequest {
        key: key,
        users: body.users,
    };

    let mut request = tonic::Request::new(request);
    set_headers(&mut request, id);

    let response = match cl.grant(request).await {
        Ok(response) => response,
        Err(status) => return Err(super::status_to_rejection(status)),
    };

    let response = response.into_inner();
    Ok(warp::reply::json(&response.updated))
}

async fn handle_revoke(
    cl: Client,
    id: Identity,
    key: u32,
    body: ACLUsersRequest,
) -> Result<impl warp::Reply, Rejection> {
    let mut cl = cl.clone();

    let request = AclUsersRequest {
        key: key,
        users: body.users,
    };

    let mut request = tonic::Request::new(request);
    set_headers(&mut request, id);

    let response = match cl.revoke(request).await {
        Ok(response) => response,
        Err(status) => return Err(super::status_to_rejection(status)),
    };

    let response = response.into_inner();
    Ok(warp::reply::json(&response.updated))
}

#[derive(Serialize)]
struct ACL {
    perm: String,
    users: Vec<u64>,
}

#[derive(Serialize)]
struct ListResult {
    key: u32,
    acl: ACL,
}

async fn handle_list(cl: Client, id: Identity) -> Result<impl warp::Reply, Rejection> {
    let mut cl = cl.clone();

    let mut request = tonic::Request::new(AclListRequest {});
    set_headers(&mut request, id);

    let response = match cl.list(request).await {
        Ok(response) => response,
        Err(status) => return Err(super::status_to_rejection(status)),
    };
    let response = response.into_inner();

    use tokio::stream::StreamExt;
    let response = response.map(|entry| -> Result<String, Error> {
        let entry = entry?;
        let acl = entry.acl.unwrap();
        let data = ListResult {
            key: entry.key,
            acl: ACL {
                perm: acl.perm,
                users: acl.users,
            },
        };
        Ok(serde_json::to_string(&data)?)
    });

    let body = Body::wrap_stream(response);

    Ok(warp::reply::Response::new(body))
}

fn with_client(
    cl: Client,
) -> impl Filter<Extract = (Client,), Error = std::convert::Infallible> + Clone {
    warp::any().map(move || cl.clone())
}

fn with_identity(
    id: Identity,
) -> impl Filter<Extract = (Identity,), Error = std::convert::Infallible> + Clone {
    warp::any().map(move || id.clone())
}

pub fn router(
    id: Identity,
    cl: Client,
) -> impl Filter<Extract = impl warp::Reply, Error = Rejection> + Clone {
    let base = warp::any()
        .and(with_client(cl.clone()))
        .and(with_identity(id.clone()));

    let create = base
        .clone()
        .and(warp::post())
        .and(warp::body::content_length_limit(4 * 1024 * 1024)) // setting a limit of 4MB
        .and(warp::body::json())
        .and_then(handle_create);

    let list = base.clone().and(warp::get()).and_then(handle_list);

    let get = base
        .clone()
        .and(warp::path::param::<u32>()) // key
        .and(warp::get())
        .and_then(handle_get);

    let set = base
        .clone()
        .and(warp::path::param::<u32>()) // key
        .and(warp::put())
        .and(warp::body::content_length_limit(4 * 1024 * 1024)) // setting a limit of 4MB
        .and(warp::body::json())
        .and_then(handle_set);

    let grant = base
        .clone()
        .and(warp::path!(u32 / "grant"))
        .and(warp::post())
        .and(warp::body::content_length_limit(4 * 1024 * 1024)) // setting a limit of 4MB
        .and(warp::body::json())
        .and_then(handle_grant);

    let revoke = base
        .clone()
        .and(warp::path!(u32 / "revoke"))
        .and(warp::post())
        .and(warp::body::content_length_limit(4 * 1024 * 1024)) // setting a limit of 4MB
        .and(warp::body::json())
        .and_then(handle_revoke);

    warp::path("acl").and(set.or(grant).or(revoke).or(get).or(list).or(create))
}
