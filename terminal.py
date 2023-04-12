import pika
import matplotlib.pyplot as plt


class Terminal():
        def __init__(self):
            self.channel = pika.BlockingConnection(pika.ConnectionParameters('162.246.254.134')).channel()
            self.channel.exchange_declare(exchange='logs',
                                          exchange_type='fanout')
            self.channel.queue_bind(exchange='logs', queue='proxy-terminal')

        def printValues(self, time, data):
            # Crear una figura y un eje
            fig, ax = plt.subplots()

            # Crear la gráfica con los valores de tiempo y wellness
            ax.plot(time, data)

            # Agregar etiquetas y título a la gráfica
            ax.set_xlabel('Tiempo')
            ax.set_ylabel('Wellness')
            ax.set_title('Gráfica de Wellness en el Tiempo')

            # Mostrar la gráfica
            plt.show()
        def run(self):
            def callback(ch, method, properties, body):
                print(" [x] Received %r" % body)
                self.printValues([body['timestamp']], [body['wellness']])
            while True:
