from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AirAnalysisResponse(_message.Message):
    __slots__ = ["humidity", "temperature", "time"]
    HUMIDITY_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    humidity: float
    temperature: float
    time: float
    def __init__(self, temperature: _Optional[float] = ..., humidity: _Optional[float] = ..., time: _Optional[float] = ...) -> None: ...

class PollutionAnalysisResponse(_message.Message):
    __slots__ = ["co2", "time"]
    CO2_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    co2: float
    time: float
    def __init__(self, co2: _Optional[float] = ..., time: _Optional[float] = ...) -> None: ...
