// Code generated by protoc-gen-go. DO NOT EDIT.
// source: bcdb.proto

package bcdb

import (
	context "context"
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion3 // please upgrade the proto package

// Tag is a single entry in an object.
// The tag key must be a string, but the
// value can be either a string, double signed, or unsigned number
// Tags are always indexed, and can be used to find the associated meta
// objects later on.
type Tag struct {
	// key of the tag
	Key string `protobuf:"bytes,1,opt,name=key,proto3" json:"key,omitempty"`
	// value of the tag. Only supporting few primitive types
	//
	// Types that are valid to be assigned to Value:
	//	*Tag_String_
	//	*Tag_Double
	//	*Tag_Number
	//	*Tag_Unsigned
	Value                isTag_Value `protobuf_oneof:"value"`
	XXX_NoUnkeyedLiteral struct{}    `json:"-"`
	XXX_unrecognized     []byte      `json:"-"`
	XXX_sizecache        int32       `json:"-"`
}

func (m *Tag) Reset()         { *m = Tag{} }
func (m *Tag) String() string { return proto.CompactTextString(m) }
func (*Tag) ProtoMessage()    {}
func (*Tag) Descriptor() ([]byte, []int) {
	return fileDescriptor_41b705b2a83eae7f, []int{0}
}

func (m *Tag) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Tag.Unmarshal(m, b)
}
func (m *Tag) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Tag.Marshal(b, m, deterministic)
}
func (m *Tag) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Tag.Merge(m, src)
}
func (m *Tag) XXX_Size() int {
	return xxx_messageInfo_Tag.Size(m)
}
func (m *Tag) XXX_DiscardUnknown() {
	xxx_messageInfo_Tag.DiscardUnknown(m)
}

var xxx_messageInfo_Tag proto.InternalMessageInfo

func (m *Tag) GetKey() string {
	if m != nil {
		return m.Key
	}
	return ""
}

type isTag_Value interface {
	isTag_Value()
}

type Tag_String_ struct {
	String_ string `protobuf:"bytes,2,opt,name=string,proto3,oneof"`
}

type Tag_Double struct {
	Double float64 `protobuf:"fixed64,3,opt,name=double,proto3,oneof"`
}

type Tag_Number struct {
	Number int64 `protobuf:"varint,4,opt,name=number,proto3,oneof"`
}

type Tag_Unsigned struct {
	Unsigned uint64 `protobuf:"varint,5,opt,name=unsigned,proto3,oneof"`
}

func (*Tag_String_) isTag_Value() {}

func (*Tag_Double) isTag_Value() {}

func (*Tag_Number) isTag_Value() {}

func (*Tag_Unsigned) isTag_Value() {}

func (m *Tag) GetValue() isTag_Value {
	if m != nil {
		return m.Value
	}
	return nil
}

func (m *Tag) GetString_() string {
	if x, ok := m.GetValue().(*Tag_String_); ok {
		return x.String_
	}
	return ""
}

func (m *Tag) GetDouble() float64 {
	if x, ok := m.GetValue().(*Tag_Double); ok {
		return x.Double
	}
	return 0
}

func (m *Tag) GetNumber() int64 {
	if x, ok := m.GetValue().(*Tag_Number); ok {
		return x.Number
	}
	return 0
}

func (m *Tag) GetUnsigned() uint64 {
	if x, ok := m.GetValue().(*Tag_Unsigned); ok {
		return x.Unsigned
	}
	return 0
}

// XXX_OneofWrappers is for the internal use of the proto package.
func (*Tag) XXX_OneofWrappers() []interface{} {
	return []interface{}{
		(*Tag_String_)(nil),
		(*Tag_Double)(nil),
		(*Tag_Number)(nil),
		(*Tag_Unsigned)(nil),
	}
}

// Metadata represents a set of tags (also known as Metadata)
type Metadata struct {
	Tags                 []*Tag   `protobuf:"bytes,1,rep,name=tags,proto3" json:"tags,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *Metadata) Reset()         { *m = Metadata{} }
func (m *Metadata) String() string { return proto.CompactTextString(m) }
func (*Metadata) ProtoMessage()    {}
func (*Metadata) Descriptor() ([]byte, []int) {
	return fileDescriptor_41b705b2a83eae7f, []int{1}
}

func (m *Metadata) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Metadata.Unmarshal(m, b)
}
func (m *Metadata) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Metadata.Marshal(b, m, deterministic)
}
func (m *Metadata) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Metadata.Merge(m, src)
}
func (m *Metadata) XXX_Size() int {
	return xxx_messageInfo_Metadata.Size(m)
}
func (m *Metadata) XXX_DiscardUnknown() {
	xxx_messageInfo_Metadata.DiscardUnknown(m)
}

var xxx_messageInfo_Metadata proto.InternalMessageInfo

func (m *Metadata) GetTags() []*Tag {
	if m != nil {
		return m.Tags
	}
	return nil
}

// Set request
type SetRequest struct {
	Metadata             *Metadata `protobuf:"bytes,1,opt,name=metadata,proto3" json:"metadata,omitempty"`
	Data                 []byte    `protobuf:"bytes,2,opt,name=data,proto3" json:"data,omitempty"`
	XXX_NoUnkeyedLiteral struct{}  `json:"-"`
	XXX_unrecognized     []byte    `json:"-"`
	XXX_sizecache        int32     `json:"-"`
}

func (m *SetRequest) Reset()         { *m = SetRequest{} }
func (m *SetRequest) String() string { return proto.CompactTextString(m) }
func (*SetRequest) ProtoMessage()    {}
func (*SetRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_41b705b2a83eae7f, []int{2}
}

func (m *SetRequest) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_SetRequest.Unmarshal(m, b)
}
func (m *SetRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_SetRequest.Marshal(b, m, deterministic)
}
func (m *SetRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_SetRequest.Merge(m, src)
}
func (m *SetRequest) XXX_Size() int {
	return xxx_messageInfo_SetRequest.Size(m)
}
func (m *SetRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_SetRequest.DiscardUnknown(m)
}

var xxx_messageInfo_SetRequest proto.InternalMessageInfo

func (m *SetRequest) GetMetadata() *Metadata {
	if m != nil {
		return m.Metadata
	}
	return nil
}

func (m *SetRequest) GetData() []byte {
	if m != nil {
		return m.Data
	}
	return nil
}

// Set response
type SetResponse struct {
	Id                   string   `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *SetResponse) Reset()         { *m = SetResponse{} }
func (m *SetResponse) String() string { return proto.CompactTextString(m) }
func (*SetResponse) ProtoMessage()    {}
func (*SetResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_41b705b2a83eae7f, []int{3}
}

func (m *SetResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_SetResponse.Unmarshal(m, b)
}
func (m *SetResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_SetResponse.Marshal(b, m, deterministic)
}
func (m *SetResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_SetResponse.Merge(m, src)
}
func (m *SetResponse) XXX_Size() int {
	return xxx_messageInfo_SetResponse.Size(m)
}
func (m *SetResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_SetResponse.DiscardUnknown(m)
}

var xxx_messageInfo_SetResponse proto.InternalMessageInfo

func (m *SetResponse) GetId() string {
	if m != nil {
		return m.Id
	}
	return ""
}

// Get request
type GetRequest struct {
	Id                   string   `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *GetRequest) Reset()         { *m = GetRequest{} }
func (m *GetRequest) String() string { return proto.CompactTextString(m) }
func (*GetRequest) ProtoMessage()    {}
func (*GetRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_41b705b2a83eae7f, []int{4}
}

func (m *GetRequest) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_GetRequest.Unmarshal(m, b)
}
func (m *GetRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_GetRequest.Marshal(b, m, deterministic)
}
func (m *GetRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_GetRequest.Merge(m, src)
}
func (m *GetRequest) XXX_Size() int {
	return xxx_messageInfo_GetRequest.Size(m)
}
func (m *GetRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_GetRequest.DiscardUnknown(m)
}

var xxx_messageInfo_GetRequest proto.InternalMessageInfo

func (m *GetRequest) GetId() string {
	if m != nil {
		return m.Id
	}
	return ""
}

// Get response
type GetResponse struct {
	Metadata             *Metadata `protobuf:"bytes,1,opt,name=metadata,proto3" json:"metadata,omitempty"`
	Data                 []byte    `protobuf:"bytes,2,opt,name=data,proto3" json:"data,omitempty"`
	XXX_NoUnkeyedLiteral struct{}  `json:"-"`
	XXX_unrecognized     []byte    `json:"-"`
	XXX_sizecache        int32     `json:"-"`
}

func (m *GetResponse) Reset()         { *m = GetResponse{} }
func (m *GetResponse) String() string { return proto.CompactTextString(m) }
func (*GetResponse) ProtoMessage()    {}
func (*GetResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_41b705b2a83eae7f, []int{5}
}

func (m *GetResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_GetResponse.Unmarshal(m, b)
}
func (m *GetResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_GetResponse.Marshal(b, m, deterministic)
}
func (m *GetResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_GetResponse.Merge(m, src)
}
func (m *GetResponse) XXX_Size() int {
	return xxx_messageInfo_GetResponse.Size(m)
}
func (m *GetResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_GetResponse.DiscardUnknown(m)
}

var xxx_messageInfo_GetResponse proto.InternalMessageInfo

func (m *GetResponse) GetMetadata() *Metadata {
	if m != nil {
		return m.Metadata
	}
	return nil
}

func (m *GetResponse) GetData() []byte {
	if m != nil {
		return m.Data
	}
	return nil
}

// Update request
type UpdateRequest struct {
	Id                   string    `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
	Metadata             *Metadata `protobuf:"bytes,2,opt,name=metadata,proto3" json:"metadata,omitempty"`
	XXX_NoUnkeyedLiteral struct{}  `json:"-"`
	XXX_unrecognized     []byte    `json:"-"`
	XXX_sizecache        int32     `json:"-"`
}

func (m *UpdateRequest) Reset()         { *m = UpdateRequest{} }
func (m *UpdateRequest) String() string { return proto.CompactTextString(m) }
func (*UpdateRequest) ProtoMessage()    {}
func (*UpdateRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_41b705b2a83eae7f, []int{6}
}

func (m *UpdateRequest) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_UpdateRequest.Unmarshal(m, b)
}
func (m *UpdateRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_UpdateRequest.Marshal(b, m, deterministic)
}
func (m *UpdateRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_UpdateRequest.Merge(m, src)
}
func (m *UpdateRequest) XXX_Size() int {
	return xxx_messageInfo_UpdateRequest.Size(m)
}
func (m *UpdateRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_UpdateRequest.DiscardUnknown(m)
}

var xxx_messageInfo_UpdateRequest proto.InternalMessageInfo

func (m *UpdateRequest) GetId() string {
	if m != nil {
		return m.Id
	}
	return ""
}

func (m *UpdateRequest) GetMetadata() *Metadata {
	if m != nil {
		return m.Metadata
	}
	return nil
}

// Update response
type UpdateResponse struct {
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *UpdateResponse) Reset()         { *m = UpdateResponse{} }
func (m *UpdateResponse) String() string { return proto.CompactTextString(m) }
func (*UpdateResponse) ProtoMessage()    {}
func (*UpdateResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_41b705b2a83eae7f, []int{7}
}

func (m *UpdateResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_UpdateResponse.Unmarshal(m, b)
}
func (m *UpdateResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_UpdateResponse.Marshal(b, m, deterministic)
}
func (m *UpdateResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_UpdateResponse.Merge(m, src)
}
func (m *UpdateResponse) XXX_Size() int {
	return xxx_messageInfo_UpdateResponse.Size(m)
}
func (m *UpdateResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_UpdateResponse.DiscardUnknown(m)
}

var xxx_messageInfo_UpdateResponse proto.InternalMessageInfo

// Query request for finding entries
type QueryRequest struct {
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *QueryRequest) Reset()         { *m = QueryRequest{} }
func (m *QueryRequest) String() string { return proto.CompactTextString(m) }
func (*QueryRequest) ProtoMessage()    {}
func (*QueryRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_41b705b2a83eae7f, []int{8}
}

func (m *QueryRequest) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_QueryRequest.Unmarshal(m, b)
}
func (m *QueryRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_QueryRequest.Marshal(b, m, deterministic)
}
func (m *QueryRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_QueryRequest.Merge(m, src)
}
func (m *QueryRequest) XXX_Size() int {
	return xxx_messageInfo_QueryRequest.Size(m)
}
func (m *QueryRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_QueryRequest.DiscardUnknown(m)
}

var xxx_messageInfo_QueryRequest proto.InternalMessageInfo

// List response
type ListResponse struct {
	Id                   string   `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *ListResponse) Reset()         { *m = ListResponse{} }
func (m *ListResponse) String() string { return proto.CompactTextString(m) }
func (*ListResponse) ProtoMessage()    {}
func (*ListResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_41b705b2a83eae7f, []int{9}
}

func (m *ListResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_ListResponse.Unmarshal(m, b)
}
func (m *ListResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_ListResponse.Marshal(b, m, deterministic)
}
func (m *ListResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_ListResponse.Merge(m, src)
}
func (m *ListResponse) XXX_Size() int {
	return xxx_messageInfo_ListResponse.Size(m)
}
func (m *ListResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_ListResponse.DiscardUnknown(m)
}

var xxx_messageInfo_ListResponse proto.InternalMessageInfo

func (m *ListResponse) GetId() string {
	if m != nil {
		return m.Id
	}
	return ""
}

// Find response
type FindResponse struct {
	Id                   string    `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
	Metadata             *Metadata `protobuf:"bytes,2,opt,name=metadata,proto3" json:"metadata,omitempty"`
	Data                 []byte    `protobuf:"bytes,3,opt,name=data,proto3" json:"data,omitempty"`
	XXX_NoUnkeyedLiteral struct{}  `json:"-"`
	XXX_unrecognized     []byte    `json:"-"`
	XXX_sizecache        int32     `json:"-"`
}

func (m *FindResponse) Reset()         { *m = FindResponse{} }
func (m *FindResponse) String() string { return proto.CompactTextString(m) }
func (*FindResponse) ProtoMessage()    {}
func (*FindResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_41b705b2a83eae7f, []int{10}
}

func (m *FindResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_FindResponse.Unmarshal(m, b)
}
func (m *FindResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_FindResponse.Marshal(b, m, deterministic)
}
func (m *FindResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_FindResponse.Merge(m, src)
}
func (m *FindResponse) XXX_Size() int {
	return xxx_messageInfo_FindResponse.Size(m)
}
func (m *FindResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_FindResponse.DiscardUnknown(m)
}

var xxx_messageInfo_FindResponse proto.InternalMessageInfo

func (m *FindResponse) GetId() string {
	if m != nil {
		return m.Id
	}
	return ""
}

func (m *FindResponse) GetMetadata() *Metadata {
	if m != nil {
		return m.Metadata
	}
	return nil
}

func (m *FindResponse) GetData() []byte {
	if m != nil {
		return m.Data
	}
	return nil
}

func init() {
	proto.RegisterType((*Tag)(nil), "bcdb.Tag")
	proto.RegisterType((*Metadata)(nil), "bcdb.Metadata")
	proto.RegisterType((*SetRequest)(nil), "bcdb.SetRequest")
	proto.RegisterType((*SetResponse)(nil), "bcdb.SetResponse")
	proto.RegisterType((*GetRequest)(nil), "bcdb.GetRequest")
	proto.RegisterType((*GetResponse)(nil), "bcdb.GetResponse")
	proto.RegisterType((*UpdateRequest)(nil), "bcdb.UpdateRequest")
	proto.RegisterType((*UpdateResponse)(nil), "bcdb.UpdateResponse")
	proto.RegisterType((*QueryRequest)(nil), "bcdb.QueryRequest")
	proto.RegisterType((*ListResponse)(nil), "bcdb.ListResponse")
	proto.RegisterType((*FindResponse)(nil), "bcdb.FindResponse")
}

func init() {
	proto.RegisterFile("bcdb.proto", fileDescriptor_41b705b2a83eae7f)
}

var fileDescriptor_41b705b2a83eae7f = []byte{
	// 405 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0xa4, 0x53, 0x4f, 0xef, 0x93, 0x40,
	0x10, 0x65, 0x81, 0xd6, 0x76, 0x40, 0x52, 0x57, 0x0f, 0xa4, 0x69, 0x0d, 0xd9, 0x13, 0x1a, 0xd3,
	0x18, 0x8c, 0x5f, 0xa0, 0x1a, 0x69, 0x62, 0x7b, 0x90, 0xd6, 0xab, 0xc9, 0xe2, 0x6e, 0x08, 0xb1,
	0x85, 0x0a, 0x8b, 0x49, 0x8f, 0xde, 0xfd, 0xd0, 0x66, 0x59, 0xca, 0x1f, 0x4d, 0x9b, 0xfc, 0xf2,
	0xbb, 0xed, 0xbc, 0x37, 0x6f, 0x66, 0xde, 0x23, 0x00, 0xc4, 0xdf, 0x59, 0xbc, 0x3a, 0x17, 0xb9,
	0xc8, 0xb1, 0x29, 0xdf, 0xe4, 0x0f, 0x02, 0xe3, 0x40, 0x13, 0x3c, 0x03, 0xe3, 0x07, 0xbf, 0xb8,
	0xc8, 0x43, 0xfe, 0x34, 0x92, 0x4f, 0xec, 0xc2, 0xb8, 0x14, 0x45, 0x9a, 0x25, 0xae, 0x2e, 0xc1,
	0x8d, 0x16, 0x35, 0xb5, 0x64, 0x58, 0x5e, 0xc5, 0x47, 0xee, 0x1a, 0x1e, 0xf2, 0x91, 0x64, 0x54,
	0x2d, 0x99, 0xac, 0x3a, 0xc5, 0xbc, 0x70, 0x4d, 0x0f, 0xf9, 0x86, 0x64, 0x54, 0x8d, 0x17, 0x30,
	0xa9, 0xb2, 0x32, 0x4d, 0x32, 0xce, 0xdc, 0x91, 0x87, 0x7c, 0x73, 0xa3, 0x45, 0x2d, 0xb2, 0x7e,
	0x02, 0xa3, 0x5f, 0xf4, 0x58, 0x71, 0xf2, 0x0a, 0x26, 0x3b, 0x2e, 0x28, 0xa3, 0x82, 0xe2, 0x25,
	0x98, 0x82, 0x26, 0xa5, 0x8b, 0x3c, 0xc3, 0xb7, 0x82, 0xe9, 0xaa, 0xbe, 0xfd, 0x40, 0x93, 0xa8,
	0x86, 0xc9, 0x16, 0x60, 0xcf, 0x45, 0xc4, 0x7f, 0x56, 0xbc, 0x14, 0xf8, 0x35, 0x4c, 0x4e, 0x8d,
	0xb0, 0x36, 0x61, 0x05, 0x8e, 0x12, 0x5c, 0xc7, 0x45, 0x2d, 0x8f, 0x31, 0x98, 0x75, 0x9f, 0xf4,
	0x65, 0x47, 0xf5, 0x9b, 0x2c, 0xc1, 0xaa, 0xa7, 0x95, 0xe7, 0x3c, 0x2b, 0x39, 0x76, 0x40, 0x4f,
	0x59, 0x93, 0x86, 0x9e, 0x32, 0xb2, 0x00, 0x08, 0xbb, 0x65, 0xff, 0xb2, 0x3b, 0xb0, 0xc2, 0x9e,
	0xf8, 0xb1, 0xb7, 0x7c, 0x86, 0xa7, 0x5f, 0xcf, 0x8c, 0x0a, 0x7e, 0x63, 0xdf, 0x60, 0x81, 0x7e,
	0x7f, 0x01, 0x99, 0x81, 0x73, 0x1d, 0xa6, 0xce, 0x23, 0x0e, 0xd8, 0x5f, 0x2a, 0x5e, 0x5c, 0x9a,
	0xe9, 0xe4, 0x25, 0xd8, 0xdb, 0xb4, 0xbc, 0xed, 0xfd, 0x1b, 0xd8, 0x9f, 0xd2, 0x8c, 0xdd, 0xe2,
	0x1f, 0x72, 0x4d, 0x6b, 0xd7, 0xe8, 0xec, 0x06, 0xbf, 0x75, 0x30, 0xd7, 0x1f, 0x3e, 0xae, 0xf1,
	0x1b, 0x30, 0xf6, 0x5c, 0xe0, 0x99, 0x52, 0x77, 0x1f, 0x77, 0xfe, 0xac, 0x87, 0x34, 0x26, 0x34,
	0xd9, 0x1d, 0x76, 0xdd, 0xe1, 0x7f, 0xdd, 0xe1, 0xa0, 0xfb, 0x3d, 0x8c, 0x55, 0x0c, 0xf8, 0xb9,
	0xa2, 0x07, 0x09, 0xcf, 0x5f, 0x0c, 0xc1, 0x56, 0x16, 0x80, 0x29, 0xb3, 0xc1, 0x58, 0xf1, 0xfd,
	0xdc, 0xe6, 0x0d, 0xd6, 0xcf, 0x8e, 0x68, 0x6f, 0x91, 0xd4, 0xc8, 0xbc, 0xee, 0x69, 0xfa, 0x79,
	0x4a, 0x4d, 0x3c, 0xae, 0xff, 0xc9, 0x77, 0x7f, 0x03, 0x00, 0x00, 0xff, 0xff, 0xb6, 0xda, 0x70,
	0x3f, 0xa1, 0x03, 0x00, 0x00,
}

// Reference imports to suppress errors if they are not otherwise used.
var _ context.Context
var _ grpc.ClientConnInterface

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
const _ = grpc.SupportPackageIsVersion6

// BCDBClient is the client API for BCDB service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://godoc.org/google.golang.org/grpc#ClientConn.NewStream.
type BCDBClient interface {
	// Set stores a document and return a header
	Set(ctx context.Context, in *SetRequest, opts ...grpc.CallOption) (*SetResponse, error)
	// Get a document from header
	Get(ctx context.Context, in *GetRequest, opts ...grpc.CallOption) (*GetResponse, error)
	// Modify updates a document meta
	Update(ctx context.Context, in *UpdateRequest, opts ...grpc.CallOption) (*UpdateResponse, error)
	// List returns a list of document IDs that matches a query
	List(ctx context.Context, in *QueryRequest, opts ...grpc.CallOption) (BCDB_ListClient, error)
	// Find like list but return full documents
	Find(ctx context.Context, in *QueryRequest, opts ...grpc.CallOption) (BCDB_FindClient, error)
}

type bCDBClient struct {
	cc grpc.ClientConnInterface
}

func NewBCDBClient(cc grpc.ClientConnInterface) BCDBClient {
	return &bCDBClient{cc}
}

func (c *bCDBClient) Set(ctx context.Context, in *SetRequest, opts ...grpc.CallOption) (*SetResponse, error) {
	out := new(SetResponse)
	err := c.cc.Invoke(ctx, "/bcdb.BCDB/Set", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *bCDBClient) Get(ctx context.Context, in *GetRequest, opts ...grpc.CallOption) (*GetResponse, error) {
	out := new(GetResponse)
	err := c.cc.Invoke(ctx, "/bcdb.BCDB/Get", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *bCDBClient) Update(ctx context.Context, in *UpdateRequest, opts ...grpc.CallOption) (*UpdateResponse, error) {
	out := new(UpdateResponse)
	err := c.cc.Invoke(ctx, "/bcdb.BCDB/Update", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *bCDBClient) List(ctx context.Context, in *QueryRequest, opts ...grpc.CallOption) (BCDB_ListClient, error) {
	stream, err := c.cc.NewStream(ctx, &_BCDB_serviceDesc.Streams[0], "/bcdb.BCDB/List", opts...)
	if err != nil {
		return nil, err
	}
	x := &bCDBListClient{stream}
	if err := x.ClientStream.SendMsg(in); err != nil {
		return nil, err
	}
	if err := x.ClientStream.CloseSend(); err != nil {
		return nil, err
	}
	return x, nil
}

type BCDB_ListClient interface {
	Recv() (*ListResponse, error)
	grpc.ClientStream
}

type bCDBListClient struct {
	grpc.ClientStream
}

func (x *bCDBListClient) Recv() (*ListResponse, error) {
	m := new(ListResponse)
	if err := x.ClientStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

func (c *bCDBClient) Find(ctx context.Context, in *QueryRequest, opts ...grpc.CallOption) (BCDB_FindClient, error) {
	stream, err := c.cc.NewStream(ctx, &_BCDB_serviceDesc.Streams[1], "/bcdb.BCDB/Find", opts...)
	if err != nil {
		return nil, err
	}
	x := &bCDBFindClient{stream}
	if err := x.ClientStream.SendMsg(in); err != nil {
		return nil, err
	}
	if err := x.ClientStream.CloseSend(); err != nil {
		return nil, err
	}
	return x, nil
}

type BCDB_FindClient interface {
	Recv() (*FindResponse, error)
	grpc.ClientStream
}

type bCDBFindClient struct {
	grpc.ClientStream
}

func (x *bCDBFindClient) Recv() (*FindResponse, error) {
	m := new(FindResponse)
	if err := x.ClientStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

// BCDBServer is the server API for BCDB service.
type BCDBServer interface {
	// Set stores a document and return a header
	Set(context.Context, *SetRequest) (*SetResponse, error)
	// Get a document from header
	Get(context.Context, *GetRequest) (*GetResponse, error)
	// Modify updates a document meta
	Update(context.Context, *UpdateRequest) (*UpdateResponse, error)
	// List returns a list of document IDs that matches a query
	List(*QueryRequest, BCDB_ListServer) error
	// Find like list but return full documents
	Find(*QueryRequest, BCDB_FindServer) error
}

// UnimplementedBCDBServer can be embedded to have forward compatible implementations.
type UnimplementedBCDBServer struct {
}

func (*UnimplementedBCDBServer) Set(ctx context.Context, req *SetRequest) (*SetResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Set not implemented")
}
func (*UnimplementedBCDBServer) Get(ctx context.Context, req *GetRequest) (*GetResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Get not implemented")
}
func (*UnimplementedBCDBServer) Update(ctx context.Context, req *UpdateRequest) (*UpdateResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Update not implemented")
}
func (*UnimplementedBCDBServer) List(req *QueryRequest, srv BCDB_ListServer) error {
	return status.Errorf(codes.Unimplemented, "method List not implemented")
}
func (*UnimplementedBCDBServer) Find(req *QueryRequest, srv BCDB_FindServer) error {
	return status.Errorf(codes.Unimplemented, "method Find not implemented")
}

func RegisterBCDBServer(s *grpc.Server, srv BCDBServer) {
	s.RegisterService(&_BCDB_serviceDesc, srv)
}

func _BCDB_Set_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(SetRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(BCDBServer).Set(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/bcdb.BCDB/Set",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(BCDBServer).Set(ctx, req.(*SetRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _BCDB_Get_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(BCDBServer).Get(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/bcdb.BCDB/Get",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(BCDBServer).Get(ctx, req.(*GetRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _BCDB_Update_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(UpdateRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(BCDBServer).Update(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/bcdb.BCDB/Update",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(BCDBServer).Update(ctx, req.(*UpdateRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _BCDB_List_Handler(srv interface{}, stream grpc.ServerStream) error {
	m := new(QueryRequest)
	if err := stream.RecvMsg(m); err != nil {
		return err
	}
	return srv.(BCDBServer).List(m, &bCDBListServer{stream})
}

type BCDB_ListServer interface {
	Send(*ListResponse) error
	grpc.ServerStream
}

type bCDBListServer struct {
	grpc.ServerStream
}

func (x *bCDBListServer) Send(m *ListResponse) error {
	return x.ServerStream.SendMsg(m)
}

func _BCDB_Find_Handler(srv interface{}, stream grpc.ServerStream) error {
	m := new(QueryRequest)
	if err := stream.RecvMsg(m); err != nil {
		return err
	}
	return srv.(BCDBServer).Find(m, &bCDBFindServer{stream})
}

type BCDB_FindServer interface {
	Send(*FindResponse) error
	grpc.ServerStream
}

type bCDBFindServer struct {
	grpc.ServerStream
}

func (x *bCDBFindServer) Send(m *FindResponse) error {
	return x.ServerStream.SendMsg(m)
}

var _BCDB_serviceDesc = grpc.ServiceDesc{
	ServiceName: "bcdb.BCDB",
	HandlerType: (*BCDBServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "Set",
			Handler:    _BCDB_Set_Handler,
		},
		{
			MethodName: "Get",
			Handler:    _BCDB_Get_Handler,
		},
		{
			MethodName: "Update",
			Handler:    _BCDB_Update_Handler,
		},
	},
	Streams: []grpc.StreamDesc{
		{
			StreamName:    "List",
			Handler:       _BCDB_List_Handler,
			ServerStreams: true,
		},
		{
			StreamName:    "Find",
			Handler:       _BCDB_Find_Handler,
			ServerStreams: true,
		},
	},
	Metadata: "bcdb.proto",
}
