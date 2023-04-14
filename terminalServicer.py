from concurrent import futures
import datetime

import grpc
import time
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pickle

import redis

from gRPC.PROTO import terminal_pb2, terminal_pb2_grpc


class TerminalServiceServicer(terminal_pb2_grpc.TerminalServiceServicer):
    def __init__(self):
        self.times = []
        self.avgs = []
        self.desvs = []
        self.start_time = float(datetime.datetime.now().timestamp())
    def SendWellnessResults(self, request, context):
        print(f'received from terminal server {request.time}, {request.avg}, {request.desv}')

        # Add request data to lists
        self.times.append(request.time)
        self.avgs.append(request.avg)
        self.desvs.append(request.desv)

        # Plot the diagram
        fig, ax = plt.subplots()
        ax.plot(self.times, self.avgs, label='avg')
        ax.plot(self.times, self.desvs, label='desv')
        ax.legend()
        ax.set(xlabel='time', ylabel='value')
        xlabels = [times - self.start_time for times in self.times]
        ax.set_xticklabels([f'{x:.2f}s' for x in xlabels])
        print('showing diagram')
        plt.show(block=False)
        plt.pause(0.001)

        response = terminal_pb2_grpc.google_dot_protobuf_dot_empty__pb2.Empty()
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    terminal_pb2_grpc.add_TerminalServiceServicer_to_server(TerminalServiceServicer(), server)
    server.add_insecure_port('0.0.0.0:5006')
    server.start()
    print('TERMINAL server started')
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
