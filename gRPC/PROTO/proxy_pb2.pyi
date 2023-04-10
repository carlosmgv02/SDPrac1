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

class WellnessResults(_message.Message):
    __slots__ = ["avgCo2", "avgMeteo", "desvCo2", "desvMeteo", "regCo2", "regMeteo", "wellnessCo2", "wellnessMeteo"]
    AVGCO2_FIELD_NUMBER: _ClassVar[int]
    AVGMETEO_FIELD_NUMBER: _ClassVar[int]
    DESVCO2_FIELD_NUMBER: _ClassVar[int]
    DESVMETEO_FIELD_NUMBER: _ClassVar[int]
    REGCO2_FIELD_NUMBER: _ClassVar[int]
    REGMETEO_FIELD_NUMBER: _ClassVar[int]
    WELLNESSCO2_FIELD_NUMBER: _ClassVar[int]
    WELLNESSMETEO_FIELD_NUMBER: _ClassVar[int]
    avgCo2: float
    avgMeteo: float
    desvCo2: float
    desvMeteo: float
    regCo2: float
    regMeteo: float
    wellnessCo2: float
    wellnessMeteo: float
    def __init__(self, wellnessCo2: _Optional[float] = ..., wellnessMeteo: _Optional[float] = ..., avgCo2: _Optional[float] = ..., avgMeteo: _Optional[float] = ..., desvCo2: _Optional[float] = ..., desvMeteo: _Optional[float] = ..., regCo2: _Optional[float] = ..., regMeteo: _Optional[float] = ...) -> None: ...
