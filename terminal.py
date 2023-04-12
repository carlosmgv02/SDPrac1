import pika
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from jsonpickle import json
from datetime import datetime


class Terminal():
    def __init__(self):
        self.channel = pika.BlockingConnection(pika.ConnectionParameters('162.246.254.134')).channel()
        self.channel.exchange_declare(exchange='logs', exchange_type='fanout')
        result = self.channel.queue_declare(queue='', exclusive=True)
        self.queue_name = result.method.queue
        self.channel.queue_bind(exchange='logs', queue=self.queue_name)

        # Crear una figura y un eje
        self.fig, self.ax = plt.subplots()

        # Agregar etiquetas y título a la gráfica
        self.ax.set_xlabel('Tiempo')
        self.ax.set_ylabel('Media')
        self.ax.set_title('Gráfica de Wellness en el Tiempo')

        # Configurar el formato de la etiqueta del eje X
        self.ax.xaxis.set_major_formatter(mdates.DateFormatter(' %H:%M:%S'))

    def printValues(self, time, data):
        # Convertir el objeto datetime a un objeto matplotlib.dates
        time = mdates.date2num(time)
        # Actualizar la gráfica con los nuevos valores de tiempo y data
        self.ax.plot_date(time, data, linestyle='-', color='b')
        plt.draw()
        plt.pause(0.001)

    def run(self):
        def callback(ch, method, properties, body):
            print(" [x] Received %r" % body)
            data = json.loads(body)
            time = datetime.strptime(data['time'], '%Y-%m-%d %H:%M:%S')
            self.printValues(time, [data['average']])

        self.channel.basic_consume(queue=self.queue_name, on_message_callback=callback, auto_ack=True)
        self.channel.start_consuming()


if __name__ == '__main__':
    print('TERMINAL')
    terminal = Terminal()
    terminal.run()
