from concurrent import futures
import grpc
import time

from gRPC.PROTO import proxy_pb2, proxy_pb2_grpc
from loadBalancer import RRLB
from meteo_utils import MeteoDataDetector


class ProxyServicer(proxy_pb2_grpc.ProxyServicer):

    def GetPollution(self, request, context):
        # Here you can write your implementation to analyze the pollution level
        # For example, let's say you want to return some dummy data
        print('desde procsi polusion' + str(request))

        response = proxy_pb2_grpc.google_dot_protobuf_dot_empty__pb2.Empty()
        return response

    def GetMeteo(self, request, context):
        # Here you can write your implementation to analyze the air quality
        # For example, let's say you want to return some dummy data
        print('desde procsi' + str(request))
        response = proxy_pb2_grpc.google_dot_protobuf_dot_empty__pb2.Empty()
        return response

    def SendWellnessResults(self, request, context):
        # Here you can write your implementation to send the wellness results
        # For example, let's say you want to return some dummy data
        wellness_results = proxy_pb2.WellnessResults(wellnessCo2=1.0, wellnessMeteo=2.0,
                                                     avgCo2=3.0, avgMeteo=4.0,
                                                     desvCo2=5.0, desvMeteo=6.0,
                                                     regCo2=7.0, regMeteo=8.0)
        return wellness_results


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    proxy_pb2_grpc.add_ProxyServicerServicer_to_server(ProxyServicer(), server)
    server.add_insecure_port('0.0.0.0:5004')
    server.start()
    try:
        while True:
            print('Server running on port 5004')
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
