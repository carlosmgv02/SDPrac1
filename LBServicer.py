from concurrent import futures
import datetime

import grpc
import time

import meteo_utils
from gRPC.PROTO import meteo_utils_pb2_grpc, meteo_utils_pb2
from gRPC.PROTO import load_balancer_pb2_grpc

from loadBalancer import RRLB


class LoadBalancerServicer(load_balancer_pb2_grpc.LoadBalancerServicer):

    def SendMeteoData(self, request, context):
        channel = grpc.insecure_channel(RRLB.get_next_address())
        stub = load_balancer_pb2_grpc.MeteoDataServiceStub(channel)
        return stub.sendMeteoData(request)

    def SendMeteoPollutionData(self, request, context):
        channel = grpc.insecure_channel(RRLB.get_next_address())
        stub = load_balancer_pb2_grpc.MeteoDataServiceStub(channel)
        return stub.sendMeteoPollutionData(request)

    def ReceiveMeteo(self, request, context):
        channel = RRLB.receive_meteo_channel()
        print(str(request) + 'will be processed in ' + channel)
        channel_stub = grpc.insecure_channel(channel)
        RRLB.set_server(channel)
        server_processor_meteo = meteo_utils_pb2_grpc.MeteoDataServiceStub(channel_stub)
        #print('this is the response' +`)
        #response_processor_meteo = server_processor_meteo.ProcessMeteoData(request)
        response = load_balancer_pb2_grpc.google_dot_protobuf_dot_empty__pb2.Empty()
        return response

    def ReceivePollution(self, request, context):
        channel = RRLB.receive_pollution_channel()

        print(str(request.time) + 'will be processed in ' + channel)
        # server_processor_pollution = meteo_utils_pb2_grpc.MeteoDataServiceStub(channel)
        # response_processor_meteo = server_processor_pollution.ProcessPollutionData(request)
        response = load_balancer_pb2_grpc.google_dot_protobuf_dot_empty__pb2.Empty()
        return response

    def AnalyzeAir(self, empty, context):
        # Here you can write your implementation to analyze the air quality
        # For example, let's say you want to return some dummy data
        detector = meteo_utils.MeteoDataDetector()
        meteo_data = detector.analyze_air()
        # temperature=20.0, humidity=3.0
        response = meteo_utils_pb2.AirAnalysisResponse(temperature=meteo_data["humidity"],
                                                       humidity=meteo_data["temperature"])
        return response

    def AnalyzePollution(self, empty, context):
        # Here you can write your implementation to analyze the pollution level
        # For example, let's say you want to return some dummy data
        detector = meteo_utils.MeteoDataDetector()
        meteo_data = detector.analyze_pollution()
        response = meteo_utils_pb2.PollutionAnalysisResponse(co2=meteo_data["co2"])
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    load_balancer_pb2_grpc.add_LoadBalancerServicerServicer_to_server(
        LoadBalancerServicer(), server)
    server.add_insecure_port("[::]:50050")
    server.start()
    try:
        while True:
            print('Funcionant')
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
