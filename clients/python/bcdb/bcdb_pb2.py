# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bcdb.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='bcdb.proto',
  package='bcdb',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\nbcdb.proto\x12\x04\x62\x63\x64\x62\"!\n\x03Tag\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x15\n\x06\x41\x63lRef\x12\x0b\n\x03\x61\x63l\x18\x01 \x01(\x04\"R\n\x08Metadata\x12\x17\n\x04tags\x18\x01 \x03(\x0b\x32\t.bcdb.Tag\x12\x12\n\ncollection\x18\x02 \x01(\t\x12\x19\n\x03\x61\x63l\x18\x03 \x01(\x0b\x32\x0c.bcdb.AclRef\"<\n\nSetRequest\x12 \n\x08metadata\x18\x01 \x01(\x0b\x32\x0e.bcdb.Metadata\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"\x19\n\x0bSetResponse\x12\n\n\x02id\x18\x01 \x01(\r\",\n\nGetRequest\x12\n\n\x02id\x18\x01 \x01(\r\x12\x12\n\ncollection\x18\x02 \x01(\t\"=\n\x0bGetResponse\x12 \n\x08metadata\x18\x01 \x01(\x0b\x32\x0e.bcdb.Metadata\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"=\n\rUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\r\x12 \n\x08metadata\x18\x02 \x01(\x0b\x32\x0e.bcdb.Metadata\"\x10\n\x0eUpdateResponse\";\n\x0cQueryRequest\x12\x12\n\ncollection\x18\x01 \x01(\t\x12\x17\n\x04tags\x18\x02 \x03(\x0b\x32\t.bcdb.Tag\"\x1a\n\x0cListResponse\x12\n\n\x02id\x18\x01 \x01(\r\"<\n\x0c\x46indResponse\x12\n\n\x02id\x18\x01 \x01(\r\x12 \n\x08metadata\x18\x02 \x01(\x0b\x32\x0e.bcdb.Metadata\"\"\n\x03\x41\x43L\x12\x0c\n\x04perm\x18\x01 \x01(\t\x12\r\n\x05users\x18\x02 \x03(\x04\"\x1c\n\rACLGetRequest\x12\x0b\n\x03key\x18\x01 \x01(\r\"(\n\x0e\x41\x43LGetResponse\x12\x16\n\x03\x61\x63l\x18\x01 \x01(\x0b\x32\t.bcdb.ACL\"*\n\x10\x41\x43LCreateRequest\x12\x16\n\x03\x61\x63l\x18\x01 \x01(\x0b\x32\t.bcdb.ACL\" \n\x11\x41\x43LCreateResponse\x12\x0b\n\x03key\x18\x01 \x01(\r\"\x10\n\x0e\x41\x43LListRequest\"6\n\x0f\x41\x43LListResponse\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\x16\n\x03\x61\x63l\x18\x02 \x01(\x0b\x32\t.bcdb.ACL\"*\n\rACLSetRequest\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\x0c\n\x04perm\x18\x02 \x01(\t\"\x10\n\x0e\x41\x43LSetResponse\"-\n\x0f\x41\x43LUsersRequest\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05users\x18\x02 \x03(\x04\"#\n\x10\x41\x43LUsersResponse\x12\x0f\n\x07updated\x18\x01 \x01(\x04\x32\x81\x02\n\x04\x42\x43\x44\x42\x12,\n\x03Set\x12\x10.bcdb.SetRequest\x1a\x11.bcdb.SetResponse\"\x00\x12,\n\x03Get\x12\x10.bcdb.GetRequest\x1a\x11.bcdb.GetResponse\"\x00\x12\x35\n\x06Update\x12\x13.bcdb.UpdateRequest\x1a\x14.bcdb.UpdateResponse\"\x00\x12\x32\n\x04List\x12\x12.bcdb.QueryRequest\x1a\x12.bcdb.ListResponse\"\x00\x30\x01\x12\x32\n\x04\x46ind\x12\x12.bcdb.QueryRequest\x1a\x12.bcdb.FindResponse\"\x00\x30\x01\x32\xd8\x02\n\x03\x41\x63l\x12\x32\n\x03Get\x12\x13.bcdb.ACLGetRequest\x1a\x14.bcdb.ACLGetResponse\"\x00\x12;\n\x06\x43reate\x12\x16.bcdb.ACLCreateRequest\x1a\x17.bcdb.ACLCreateResponse\"\x00\x12\x37\n\x04List\x12\x14.bcdb.ACLListRequest\x1a\x15.bcdb.ACLListResponse\"\x00\x30\x01\x12\x32\n\x03Set\x12\x13.bcdb.ACLSetRequest\x1a\x14.bcdb.ACLSetResponse\"\x00\x12\x38\n\x05Grant\x12\x15.bcdb.ACLUsersRequest\x1a\x16.bcdb.ACLUsersResponse\"\x00\x12\x39\n\x06Revoke\x12\x15.bcdb.ACLUsersRequest\x1a\x16.bcdb.ACLUsersResponse\"\x00\x62\x06proto3'
)




_TAG = _descriptor.Descriptor(
  name='Tag',
  full_name='bcdb.Tag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='bcdb.Tag.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='bcdb.Tag.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=53,
)


_ACLREF = _descriptor.Descriptor(
  name='AclRef',
  full_name='bcdb.AclRef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='acl', full_name='bcdb.AclRef.acl', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=55,
  serialized_end=76,
)


_METADATA = _descriptor.Descriptor(
  name='Metadata',
  full_name='bcdb.Metadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tags', full_name='bcdb.Metadata.tags', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collection', full_name='bcdb.Metadata.collection', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acl', full_name='bcdb.Metadata.acl', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=78,
  serialized_end=160,
)


_SETREQUEST = _descriptor.Descriptor(
  name='SetRequest',
  full_name='bcdb.SetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadata', full_name='bcdb.SetRequest.metadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='bcdb.SetRequest.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=162,
  serialized_end=222,
)


_SETRESPONSE = _descriptor.Descriptor(
  name='SetResponse',
  full_name='bcdb.SetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bcdb.SetResponse.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=224,
  serialized_end=249,
)


_GETREQUEST = _descriptor.Descriptor(
  name='GetRequest',
  full_name='bcdb.GetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bcdb.GetRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collection', full_name='bcdb.GetRequest.collection', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=251,
  serialized_end=295,
)


_GETRESPONSE = _descriptor.Descriptor(
  name='GetResponse',
  full_name='bcdb.GetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadata', full_name='bcdb.GetResponse.metadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='bcdb.GetResponse.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=297,
  serialized_end=358,
)


_UPDATEREQUEST = _descriptor.Descriptor(
  name='UpdateRequest',
  full_name='bcdb.UpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bcdb.UpdateRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='bcdb.UpdateRequest.metadata', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=360,
  serialized_end=421,
)


_UPDATERESPONSE = _descriptor.Descriptor(
  name='UpdateResponse',
  full_name='bcdb.UpdateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=423,
  serialized_end=439,
)


_QUERYREQUEST = _descriptor.Descriptor(
  name='QueryRequest',
  full_name='bcdb.QueryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='collection', full_name='bcdb.QueryRequest.collection', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='bcdb.QueryRequest.tags', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=441,
  serialized_end=500,
)


_LISTRESPONSE = _descriptor.Descriptor(
  name='ListResponse',
  full_name='bcdb.ListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bcdb.ListResponse.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=502,
  serialized_end=528,
)


_FINDRESPONSE = _descriptor.Descriptor(
  name='FindResponse',
  full_name='bcdb.FindResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bcdb.FindResponse.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='bcdb.FindResponse.metadata', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=530,
  serialized_end=590,
)


_ACL = _descriptor.Descriptor(
  name='ACL',
  full_name='bcdb.ACL',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='perm', full_name='bcdb.ACL.perm', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='users', full_name='bcdb.ACL.users', index=1,
      number=2, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=592,
  serialized_end=626,
)


_ACLGETREQUEST = _descriptor.Descriptor(
  name='ACLGetRequest',
  full_name='bcdb.ACLGetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='bcdb.ACLGetRequest.key', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=628,
  serialized_end=656,
)


_ACLGETRESPONSE = _descriptor.Descriptor(
  name='ACLGetResponse',
  full_name='bcdb.ACLGetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='acl', full_name='bcdb.ACLGetResponse.acl', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=658,
  serialized_end=698,
)


_ACLCREATEREQUEST = _descriptor.Descriptor(
  name='ACLCreateRequest',
  full_name='bcdb.ACLCreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='acl', full_name='bcdb.ACLCreateRequest.acl', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=700,
  serialized_end=742,
)


_ACLCREATERESPONSE = _descriptor.Descriptor(
  name='ACLCreateResponse',
  full_name='bcdb.ACLCreateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='bcdb.ACLCreateResponse.key', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=744,
  serialized_end=776,
)


_ACLLISTREQUEST = _descriptor.Descriptor(
  name='ACLListRequest',
  full_name='bcdb.ACLListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=778,
  serialized_end=794,
)


_ACLLISTRESPONSE = _descriptor.Descriptor(
  name='ACLListResponse',
  full_name='bcdb.ACLListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='bcdb.ACLListResponse.key', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acl', full_name='bcdb.ACLListResponse.acl', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=796,
  serialized_end=850,
)


_ACLSETREQUEST = _descriptor.Descriptor(
  name='ACLSetRequest',
  full_name='bcdb.ACLSetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='bcdb.ACLSetRequest.key', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='perm', full_name='bcdb.ACLSetRequest.perm', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=852,
  serialized_end=894,
)


_ACLSETRESPONSE = _descriptor.Descriptor(
  name='ACLSetResponse',
  full_name='bcdb.ACLSetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=896,
  serialized_end=912,
)


_ACLUSERSREQUEST = _descriptor.Descriptor(
  name='ACLUsersRequest',
  full_name='bcdb.ACLUsersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='bcdb.ACLUsersRequest.key', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='users', full_name='bcdb.ACLUsersRequest.users', index=1,
      number=2, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=914,
  serialized_end=959,
)


_ACLUSERSRESPONSE = _descriptor.Descriptor(
  name='ACLUsersResponse',
  full_name='bcdb.ACLUsersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='updated', full_name='bcdb.ACLUsersResponse.updated', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=961,
  serialized_end=996,
)

_METADATA.fields_by_name['tags'].message_type = _TAG
_METADATA.fields_by_name['acl'].message_type = _ACLREF
_SETREQUEST.fields_by_name['metadata'].message_type = _METADATA
_GETRESPONSE.fields_by_name['metadata'].message_type = _METADATA
_UPDATEREQUEST.fields_by_name['metadata'].message_type = _METADATA
_QUERYREQUEST.fields_by_name['tags'].message_type = _TAG
_FINDRESPONSE.fields_by_name['metadata'].message_type = _METADATA
_ACLGETRESPONSE.fields_by_name['acl'].message_type = _ACL
_ACLCREATEREQUEST.fields_by_name['acl'].message_type = _ACL
_ACLLISTRESPONSE.fields_by_name['acl'].message_type = _ACL
DESCRIPTOR.message_types_by_name['Tag'] = _TAG
DESCRIPTOR.message_types_by_name['AclRef'] = _ACLREF
DESCRIPTOR.message_types_by_name['Metadata'] = _METADATA
DESCRIPTOR.message_types_by_name['SetRequest'] = _SETREQUEST
DESCRIPTOR.message_types_by_name['SetResponse'] = _SETRESPONSE
DESCRIPTOR.message_types_by_name['GetRequest'] = _GETREQUEST
DESCRIPTOR.message_types_by_name['GetResponse'] = _GETRESPONSE
DESCRIPTOR.message_types_by_name['UpdateRequest'] = _UPDATEREQUEST
DESCRIPTOR.message_types_by_name['UpdateResponse'] = _UPDATERESPONSE
DESCRIPTOR.message_types_by_name['QueryRequest'] = _QUERYREQUEST
DESCRIPTOR.message_types_by_name['ListResponse'] = _LISTRESPONSE
DESCRIPTOR.message_types_by_name['FindResponse'] = _FINDRESPONSE
DESCRIPTOR.message_types_by_name['ACL'] = _ACL
DESCRIPTOR.message_types_by_name['ACLGetRequest'] = _ACLGETREQUEST
DESCRIPTOR.message_types_by_name['ACLGetResponse'] = _ACLGETRESPONSE
DESCRIPTOR.message_types_by_name['ACLCreateRequest'] = _ACLCREATEREQUEST
DESCRIPTOR.message_types_by_name['ACLCreateResponse'] = _ACLCREATERESPONSE
DESCRIPTOR.message_types_by_name['ACLListRequest'] = _ACLLISTREQUEST
DESCRIPTOR.message_types_by_name['ACLListResponse'] = _ACLLISTRESPONSE
DESCRIPTOR.message_types_by_name['ACLSetRequest'] = _ACLSETREQUEST
DESCRIPTOR.message_types_by_name['ACLSetResponse'] = _ACLSETRESPONSE
DESCRIPTOR.message_types_by_name['ACLUsersRequest'] = _ACLUSERSREQUEST
DESCRIPTOR.message_types_by_name['ACLUsersResponse'] = _ACLUSERSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Tag = _reflection.GeneratedProtocolMessageType('Tag', (_message.Message,), {
  'DESCRIPTOR' : _TAG,
  '__module__' : 'bcdb_pb2'
  # @@protoc_insertion_point(class_scope:bcdb.Tag)
  })
_sym_db.RegisterMessage(Tag)

AclRef = _reflection.GeneratedProtocolMessageType('AclRef', (_message.Message,), {
  'DESCRIPTOR' : _ACLREF,
  '__module__' : 'bcdb_pb2'
  # @@protoc_insertion_point(class_scope:bcdb.AclRef)
  })
_sym_db.RegisterMessage(AclRef)

Metadata = _reflection.GeneratedProtocolMessageType('Metadata', (_message.Message,), {
  'DESCRIPTOR' : _METADATA,
  '__module__' : 'bcdb_pb2'
  # @@protoc_insertion_point(class_scope:bcdb.Metadata)
  })
_sym_db.RegisterMessage(Metadata)

SetRequest = _reflection.GeneratedProtocolMessageType('SetRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETREQUEST,
  '__module__' : 'bcdb_pb2'
  # @@protoc_insertion_point(class_scope:bcdb.SetRequest)
  })
_sym_db.RegisterMessage(SetRequest)

SetResponse = _reflection.GeneratedProtocolMessageType('SetResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETRESPONSE,
  '__module__' : 'bcdb_pb2'
  # @@protoc_insertion_point(class_scope:bcdb.SetResponse)
  })
_sym_db.RegisterMessage(SetResponse)

GetRequest = _reflection.GeneratedProtocolMessageType('GetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETREQUEST,
  '__module__' : 'bcdb_pb2'
  # @@protoc_insertion_point(class_scope:bcdb.GetRequest)
  })
_sym_db.RegisterMessage(GetRequest)

GetResponse = _reflection.GeneratedProtocolMessageType('GetResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETRESPONSE,
  '__module__' : 'bcdb_pb2'
  # @@protoc_insertion_point(class_scope:bcdb.GetResponse)
  })
_sym_db.RegisterMessage(GetResponse)

UpdateRequest = _reflection.GeneratedProtocolMessageType('UpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEREQUEST,
  '__module__' : 'bcdb_pb2'
  # @@protoc_insertion_point(class_scope:bcdb.UpdateRequest)
  })
_sym_db.RegisterMessage(UpdateRequest)

UpdateResponse = _reflection.GeneratedProtocolMessageType('UpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATERESPONSE,
  '__module__' : 'bcdb_pb2'
  # @@protoc_insertion_point(class_scope:bcdb.UpdateResponse)
  })
_sym_db.RegisterMessage(UpdateResponse)

QueryRequest = _reflection.GeneratedProtocolMessageType('QueryRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYREQUEST,
  '__module__' : 'bcdb_pb2'
  # @@protoc_insertion_point(class_scope:bcdb.QueryRequest)
  })
_sym_db.RegisterMessage(QueryRequest)

ListResponse = _reflection.GeneratedProtocolMessageType('ListResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTRESPONSE,
  '__module__' : 'bcdb_pb2'
  # @@protoc_insertion_point(class_scope:bcdb.ListResponse)
  })
_sym_db.RegisterMessage(ListResponse)

FindResponse = _reflection.GeneratedProtocolMessageType('FindResponse', (_message.Message,), {
  'DESCRIPTOR' : _FINDRESPONSE,
  '__module__' : 'bcdb_pb2'
  # @@protoc_insertion_point(class_scope:bcdb.FindResponse)
  })
_sym_db.RegisterMessage(FindResponse)

ACL = _reflection.GeneratedProtocolMessageType('ACL', (_message.Message,), {
  'DESCRIPTOR' : _ACL,
  '__module__' : 'bcdb_pb2'
  # @@protoc_insertion_point(class_scope:bcdb.ACL)
  })
_sym_db.RegisterMessage(ACL)

ACLGetRequest = _reflection.GeneratedProtocolMessageType('ACLGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACLGETREQUEST,
  '__module__' : 'bcdb_pb2'
  # @@protoc_insertion_point(class_scope:bcdb.ACLGetRequest)
  })
_sym_db.RegisterMessage(ACLGetRequest)

ACLGetResponse = _reflection.GeneratedProtocolMessageType('ACLGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACLGETRESPONSE,
  '__module__' : 'bcdb_pb2'
  # @@protoc_insertion_point(class_scope:bcdb.ACLGetResponse)
  })
_sym_db.RegisterMessage(ACLGetResponse)

ACLCreateRequest = _reflection.GeneratedProtocolMessageType('ACLCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACLCREATEREQUEST,
  '__module__' : 'bcdb_pb2'
  # @@protoc_insertion_point(class_scope:bcdb.ACLCreateRequest)
  })
_sym_db.RegisterMessage(ACLCreateRequest)

ACLCreateResponse = _reflection.GeneratedProtocolMessageType('ACLCreateResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACLCREATERESPONSE,
  '__module__' : 'bcdb_pb2'
  # @@protoc_insertion_point(class_scope:bcdb.ACLCreateResponse)
  })
_sym_db.RegisterMessage(ACLCreateResponse)

ACLListRequest = _reflection.GeneratedProtocolMessageType('ACLListRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACLLISTREQUEST,
  '__module__' : 'bcdb_pb2'
  # @@protoc_insertion_point(class_scope:bcdb.ACLListRequest)
  })
_sym_db.RegisterMessage(ACLListRequest)

ACLListResponse = _reflection.GeneratedProtocolMessageType('ACLListResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACLLISTRESPONSE,
  '__module__' : 'bcdb_pb2'
  # @@protoc_insertion_point(class_scope:bcdb.ACLListResponse)
  })
_sym_db.RegisterMessage(ACLListResponse)

ACLSetRequest = _reflection.GeneratedProtocolMessageType('ACLSetRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACLSETREQUEST,
  '__module__' : 'bcdb_pb2'
  # @@protoc_insertion_point(class_scope:bcdb.ACLSetRequest)
  })
_sym_db.RegisterMessage(ACLSetRequest)

ACLSetResponse = _reflection.GeneratedProtocolMessageType('ACLSetResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACLSETRESPONSE,
  '__module__' : 'bcdb_pb2'
  # @@protoc_insertion_point(class_scope:bcdb.ACLSetResponse)
  })
_sym_db.RegisterMessage(ACLSetResponse)

ACLUsersRequest = _reflection.GeneratedProtocolMessageType('ACLUsersRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACLUSERSREQUEST,
  '__module__' : 'bcdb_pb2'
  # @@protoc_insertion_point(class_scope:bcdb.ACLUsersRequest)
  })
_sym_db.RegisterMessage(ACLUsersRequest)

ACLUsersResponse = _reflection.GeneratedProtocolMessageType('ACLUsersResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACLUSERSRESPONSE,
  '__module__' : 'bcdb_pb2'
  # @@protoc_insertion_point(class_scope:bcdb.ACLUsersResponse)
  })
_sym_db.RegisterMessage(ACLUsersResponse)



_BCDB = _descriptor.ServiceDescriptor(
  name='BCDB',
  full_name='bcdb.BCDB',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=999,
  serialized_end=1256,
  methods=[
  _descriptor.MethodDescriptor(
    name='Set',
    full_name='bcdb.BCDB.Set',
    index=0,
    containing_service=None,
    input_type=_SETREQUEST,
    output_type=_SETRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='bcdb.BCDB.Get',
    index=1,
    containing_service=None,
    input_type=_GETREQUEST,
    output_type=_GETRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='bcdb.BCDB.Update',
    index=2,
    containing_service=None,
    input_type=_UPDATEREQUEST,
    output_type=_UPDATERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='bcdb.BCDB.List',
    index=3,
    containing_service=None,
    input_type=_QUERYREQUEST,
    output_type=_LISTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Find',
    full_name='bcdb.BCDB.Find',
    index=4,
    containing_service=None,
    input_type=_QUERYREQUEST,
    output_type=_FINDRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_BCDB)

DESCRIPTOR.services_by_name['BCDB'] = _BCDB


_ACL = _descriptor.ServiceDescriptor(
  name='Acl',
  full_name='bcdb.Acl',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=1259,
  serialized_end=1603,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='bcdb.Acl.Get',
    index=0,
    containing_service=None,
    input_type=_ACLGETREQUEST,
    output_type=_ACLGETRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='bcdb.Acl.Create',
    index=1,
    containing_service=None,
    input_type=_ACLCREATEREQUEST,
    output_type=_ACLCREATERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='bcdb.Acl.List',
    index=2,
    containing_service=None,
    input_type=_ACLLISTREQUEST,
    output_type=_ACLLISTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Set',
    full_name='bcdb.Acl.Set',
    index=3,
    containing_service=None,
    input_type=_ACLSETREQUEST,
    output_type=_ACLSETRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Grant',
    full_name='bcdb.Acl.Grant',
    index=4,
    containing_service=None,
    input_type=_ACLUSERSREQUEST,
    output_type=_ACLUSERSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Revoke',
    full_name='bcdb.Acl.Revoke',
    index=5,
    containing_service=None,
    input_type=_ACLUSERSREQUEST,
    output_type=_ACLUSERSRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ACL)

DESCRIPTOR.services_by_name['Acl'] = _ACL

# @@protoc_insertion_point(module_scope)
