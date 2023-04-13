from concurrent import futures
import grpc
import time
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pickle

import redis

from gRPC.PROTO import terminal_pb2, terminal_pb2_grpc


class TerminalServiceServicer(terminal_pb2_grpc.TerminalServiceServicer):
    def __init__(self):
        self.requests = []

    def SendWellnessResults(self, request, context):
        print('received from terminal server' + str(request.time) + str(request.avg) + str(request.desv))

        # Store the request in a list
        self.requests.append(request)
        print('appended', self.requests)
        #Aixo no hauria de estar aki
        self.plot_avg_results()
        self.plot_desv_results()

        response = terminal_pb2_grpc.google_dot_protobuf_dot_empty__pb2.Empty()
        return response

    def plot_avg_results(self):
        times = [req.time for req in self.requests]
        avgs = [req.avg for req in self.requests]
        print('avgs: ' + str(avgs))
        print( 'times: ' + str(times))

        # Plot the diagram
        fig, ax = plt.subplots()
        ax.plot(times, avgs, label='avg')
        ax.legend()
        ax.set(xlabel='time', ylabel='value')
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
        fig.autofmt_xdate()
        print('showing avg')
        plt.show()
        plt.close()

    def plot_desv_results(self):
        times = [req.time for req in self.requests]
        desvs = [req.desv for req in self.requests]

        # Plot the diagram
        fig, ax = plt.subplots()
        ax.plot(times, desvs, label='desv')
        ax.legend()
        ax.set(xlabel='time', ylabel='value')
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
        fig.autofmt_xdate()
        print('showing avstg')

        plt.show()
        plt.close()


def serve():
    # min_time = float(min(self.redis_con.keys()))
    win_size = 5
    win_time = 5
    # max_time = min_time + win_size
    print('TERMINAL', )
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    terminal_pb2_grpc.add_TerminalServiceServicer_to_server(TerminalServiceServicer(), server)
    server.add_insecure_port('0.0.0.0:5006')
    server.start()

    try:
        while True:
            print('Server running on port 5006')
            # Call the plot_avg_results() method every win_time seconds to update the average plot
            print('calling results')
            TerminalServiceServicer().plot_avg_results()
            # Call the plot_desv_results() method every win_time seconds to update the standard deviation plot
            TerminalServiceServicer().plot_desv_results()
            time.sleep(win_time)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
