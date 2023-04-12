from concurrent import futures
import grpc
import time

import redis

from LBServicer import serve
from gRPC.PROTO import terminal_pb2, terminal_pb2_grpc
from loadBalancer import RRLB
from meteo_utils import MeteoDataDetector


class TerminalServicer(terminal_pb2_grpc.TerminalServicer):

    def GetPollution(self, request, context):
        # Here you can write your implementation to analyze the pollution level
        # For example, let's say you want to return some dummy data
        print('desde procsi polusion' + str(request))

        response = terminal_pb2_grpc.google_dot_protobuf_dot_empty__pb2.Empty()
        return response

    def GetMeteo(self, request, context):
        # Here you can write your implementation to analyze the air quality
        # For example, let's say you want to return some dummy data
        print('desde procsi' + str(request))
        response = terminal_pb2_grpc.google_dot_protobuf_dot_empty__pb2.Empty()
        return response

    def SendWellnessResults(self, request, context):
        # Here you can write your implementation to send the wellness results
        # For example, let's say you want to return some dummy data
        wellness_results = terminal.WellnessResults(wellnessCo2=1.0, wellnessMeteo=2.0,
                                                    avgCo2=3.0, avgMeteo=4.0,
                                                    desvCo2=5.0, desvMeteo=6.0,
                                                    regCo2=7.0, regMeteo=8.0)
        return wellness_results

    def serve(self):
        min_time = float(min(self.redis_con.keys()))
        win_size = 5
        win_time = 5
        while True:
            max_time = min_time + win_size
            print('Working from ', )
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        proxy_pb2_grpc.add_TerminalServicerServicer_to_server(TerminalServicer(), server)
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
