from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WellnessResults(_message.Message):
    __slots__ = ["avg", "desv", "time"]
    AVG_FIELD_NUMBER: _ClassVar[int]
    DESV_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    avg: float
    desv: float
    time: float
    def __init__(self, time: _Optional[float] = ..., avg: _Optional[float] = ..., desv: _Optional[float] = ...) -> None: ...
