# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gRPC/PROTO/terminal.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19gRPC/PROTO/terminal.proto\x1a\x1bgoogle/protobuf/empty.proto\":\n\x0fWellnessResults\x12\x0c\n\x04time\x18\x01 \x01(\x01\x12\x0b\n\x03\x61vg\x18\x02 \x01(\x02\x12\x0c\n\x04\x64\x65sv\x18\x03 \x01(\x02\x32T\n\x0fTerminalService\x12\x41\n\x13SendWellnessResults\x12\x10.WellnessResults\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gRPC.PROTO.terminal_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _WELLNESSRESULTS._serialized_start=58
  _WELLNESSRESULTS._serialized_end=116
  _TERMINALSERVICE._serialized_start=118
  _TERMINALSERVICE._serialized_end=202
# @@protoc_insertion_point(module_scope)
