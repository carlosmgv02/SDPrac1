from concurrent import futures
import grpc
import time

import redis

from LBServicer import serve
from gRPC.PROTO import terminal_pb2, terminal_pb2_grpc
from loadBalancer import RRLB
from meteo_utils import MeteoDataDetector


class TerminalServiceServicer(terminal_pb2_grpc.TerminalServiceServicer):
    def SendWellnessResults(self, request, context):
        # Here you can write your implementation to send the wellness results
        # For example, let's say you want to return some dummy data
        print('recieved from termial servier' + str(request))
        response = terminal_pb2_grpc.google_dot_protobuf_dot_empty__pb2.Empty()
        return response


def serve():
    # min_time = float(min(self.redis_con.keys()))
    win_size = 5
    win_time = 5
    # max_time = min_time + win_size
    print('Working from terminal', )
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    terminal_pb2_grpc.add_TerminalServiceServicer_to_server(TerminalServiceServicer(), server)
    server.add_insecure_port('0.0.0.0:5006')
    server.start()
    try:
        while True:
            print('Server running on port 5006')
            time.sleep(58787453)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
