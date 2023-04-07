# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import meteo_utils_pb2 as gRPC_dot_meteo__utils__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class MeteoDataServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ProcessMeteoData = channel.unary_unary(
                '/meteo.MeteoDataService/ProcessMeteoData',
                request_serializer=gRPC_dot_meteo__utils__pb2.AirAnalysisResponse.SerializeToString,
                response_deserializer=gRPC_dot_meteo__utils__pb2.AirWellness.FromString,
                )
        self.ProcessPollutionData = channel.unary_unary(
                '/meteo.MeteoDataService/ProcessPollutionData',
                request_serializer=gRPC_dot_meteo__utils__pb2.PollutionAnalysisResponse.SerializeToString,
                response_deserializer=gRPC_dot_meteo__utils__pb2.Co2Wellness.FromString,
                )
        self.AnalyzeAir = channel.unary_unary(
                '/meteo.MeteoDataService/AnalyzeAir',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=gRPC_dot_meteo__utils__pb2.AirAnalysisResponse.FromString,
                )
        self.AnalyzePollution = channel.unary_unary(
                '/meteo.MeteoDataService/AnalyzePollution',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=gRPC_dot_meteo__utils__pb2.PollutionAnalysisResponse.FromString,
                )


class MeteoDataServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ProcessMeteoData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ProcessPollutionData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AnalyzeAir(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AnalyzePollution(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MeteoDataServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ProcessMeteoData': grpc.unary_unary_rpc_method_handler(
                    servicer.ProcessMeteoData,
                    request_deserializer=gRPC_dot_meteo__utils__pb2.AirAnalysisResponse.FromString,
                    response_serializer=gRPC_dot_meteo__utils__pb2.AirWellness.SerializeToString,
            ),
            'ProcessPollutionData': grpc.unary_unary_rpc_method_handler(
                    servicer.ProcessPollutionData,
                    request_deserializer=gRPC_dot_meteo__utils__pb2.PollutionAnalysisResponse.FromString,
                    response_serializer=gRPC_dot_meteo__utils__pb2.Co2Wellness.SerializeToString,
            ),
            'AnalyzeAir': grpc.unary_unary_rpc_method_handler(
                    servicer.AnalyzeAir,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=gRPC_dot_meteo__utils__pb2.AirAnalysisResponse.SerializeToString,
            ),
            'AnalyzePollution': grpc.unary_unary_rpc_method_handler(
                    servicer.AnalyzePollution,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=gRPC_dot_meteo__utils__pb2.PollutionAnalysisResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'meteo.MeteoDataService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MeteoDataService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ProcessMeteoData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/meteo.MeteoDataService/ProcessMeteoData',
            gRPC_dot_meteo__utils__pb2.AirAnalysisResponse.SerializeToString,
            gRPC_dot_meteo__utils__pb2.AirWellness.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ProcessPollutionData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/meteo.MeteoDataService/ProcessPollutionData',
            gRPC_dot_meteo__utils__pb2.PollutionAnalysisResponse.SerializeToString,
            gRPC_dot_meteo__utils__pb2.Co2Wellness.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AnalyzeAir(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/meteo.MeteoDataService/AnalyzeAir',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            gRPC_dot_meteo__utils__pb2.AirAnalysisResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AnalyzePollution(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/meteo.MeteoDataService/AnalyzePollution',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            gRPC_dot_meteo__utils__pb2.PollutionAnalysisResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
