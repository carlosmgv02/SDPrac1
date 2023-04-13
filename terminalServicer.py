from concurrent import futures
import grpc
import time

import redis

from LBServicer import serve
from gRPC.PROTO import terminal_pb2, terminal_pb2_grpc
from loadBalancer import RRLB
from meteo_utils import MeteoDataDetector
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


class TerminalServiceServicer(terminal_pb2_grpc.TerminalServiceServicer):
    def SendWellnessResults(self, request, context):
        # Here you can write your implementation to send the wellness results
        # For example, let's say you want to return some dummy data
        print('recieved from termial servier' + str(request))
        response = terminal_pb2_grpc.google_dot_protobuf_dot_empty__pb2.Empty()

        # Crear una figura y un eje
        fig, ax = plt.subplots()

        # Agregar etiquetas y título a la gráfica
        ax.set_xlabel('Tiempo')
        ax.set_ylabel('Media')
        ax.set_title('Gráfica de Wellness en el Tiempo')

        # Configurar el formato de la etiqueta del eje X
        ax.xaxis.set_major_formatter(mdates.DateFormatter(' %H:%M:%S'))

        return response

    def printValues(self, time, data):
        # Convertir el objeto datetime a un objeto matplotlib.dates
        time = mdates.date2num(time)
        # Actualizar la gráfica con los nuevos valores de tiempo y data
        self.ax.plot_date(time, data, linestyle='-', color='b')
        plt.draw()
        plt.pause(0.001)


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
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
