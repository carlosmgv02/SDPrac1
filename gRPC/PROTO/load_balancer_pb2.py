# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gRPC/PROTO/load_balancer.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1egRPC/PROTO/load_balancer.proto\x1a\x1bgoogle/protobuf/empty.proto\"J\n\x13\x41irAnalysisResponse\x12\x13\n\x0btemperature\x18\x01 \x01(\x02\x12\x10\n\x08humidity\x18\x02 \x01(\x02\x12\x0c\n\x04time\x18\x03 \x01(\x02\"6\n\x19PollutionAnalysisResponse\x12\x0b\n\x03\x63o2\x18\x01 \x01(\x02\x12\x0c\n\x04time\x18\x03 \x01(\x02\"\x1f\n\x0b\x41irWellness\x12\x10\n\x08wellness\x18\x01 \x01(\x02\"\x1f\n\x0b\x43o2Wellness\x12\x10\n\x08wellness\x18\x01 \x01(\x02\x32\xa5\x03\n\x14LoadBalancerServicer\x12<\n\nAnalyzeAir\x12\x16.google.protobuf.Empty\x1a\x14.AirAnalysisResponse\"\x00\x12H\n\x10\x41nalyzePollution\x12\x16.google.protobuf.Empty\x1a\x1a.PollutionAnalysisResponse\"\x00\x12>\n\x0cReceiveMeteo\x12\x14.AirAnalysisResponse\x1a\x16.google.protobuf.Empty\"\x00\x12H\n\x10ReceivePollution\x12\x1a.PollutionAnalysisResponse\x1a\x16.google.protobuf.Empty\"\x00\x12\x35\n\rSendMeteoData\x12\x14.AirAnalysisResponse\x1a\x0c.AirWellness\"\x00\x12\x44\n\x16SendMeteoPollutionData\x12\x1a.PollutionAnalysisResponse\x1a\x0c.Co2Wellness\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gRPC.PROTO.load_balancer_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _AIRANALYSISRESPONSE._serialized_start=63
  _AIRANALYSISRESPONSE._serialized_end=137
  _POLLUTIONANALYSISRESPONSE._serialized_start=139
  _POLLUTIONANALYSISRESPONSE._serialized_end=193
  _AIRWELLNESS._serialized_start=195
  _AIRWELLNESS._serialized_end=226
  _CO2WELLNESS._serialized_start=228
  _CO2WELLNESS._serialized_end=259
  _LOADBALANCERSERVICER._serialized_start=262
  _LOADBALANCERSERVICER._serialized_end=683
# @@protoc_insertion_point(module_scope)
