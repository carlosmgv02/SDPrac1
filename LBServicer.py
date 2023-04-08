from concurrent import futures

import grpc
import time

import meteo_utils
from gRPC.PROTO import load_balancer_pb2_grpc, meteo_utils_pb2


class RoundRobinLoadBalancer(load_balancer_pb2_grpc.LoadBalancerServicer):
    def __init__(self, addresses):
        self.addresses = addresses
        self.current_index = 0

    def get_next_address(self):
        address = self.addresses[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.addresses)
        return address

    def sendMeteoData(self, request, context):
        channel = grpc.insecure_channel(self.get_next_address())
        stub = load_balancer_pb2_grpc.MeteoDataServiceStub(channel)
        return stub.sendMeteoData(request)

    def sendMeteoPollutionData(self, request, context):
        channel = grpc.insecure_channel(self.get_next_address())
        stub = load_balancer_pb2_grpc.MeteoDataServiceStub(channel)
        return stub.sendMeteoPollutionData(request)

    def receiveMeteo(self, request, context):
        channel = grpc.insecure_channel(self.get_next_address())
        stub = load_balancer_pb2_grpc.MeteoDataServiceStub(channel)
        return stub.receiveMeteo(request)

    def AnalyzeAir(self, request, context):
        # Here you can write your implementation to analyze the air quality
        # For example, let's say you want to return some dummy data
        detector = meteo_utils.MeteoDataDetector()
        meteo_data = detector.analyze_air()
        # temperature=20.0, humidity=3.0
        response = meteo_utils_pb2.AirAnalysisResponse(temperature=meteo_data["humidity"],
                                                       humidity=meteo_data["temperature"])
        return response

    def AnalyzePollution(self, request, context):
        # Here you can write your implementation to analyze the pollution level
        # For example, let's say you want to return some dummy data
        detector = meteo_utils.MeteoDataDetector()
        meteo_data = detector.analyze_pollution()
        response = meteo_utils_pb2.PollutionAnalysisResponse(co2=meteo_data["co2"])
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    load_balancer_pb2_grpc.add_LoadBalancerServicerServicer_to_server(
        RoundRobinLoadBalancer(["localhost:50050"]), server)
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
