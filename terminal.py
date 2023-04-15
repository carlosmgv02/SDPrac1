import pika
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from jsonpickle import json
import datetime

from numpy import double


class Terminal():
    def __init__(self):
        self.channel = pika.BlockingConnection(pika.ConnectionParameters('162.246.254.134')).channel()
        self.channel.exchange_declare(exchange='logs', exchange_type='fanout')
        result = self.channel.queue_declare(queue='', exclusive=True)
        self.queue_name = result.method.queue
        self.channel.queue_bind(exchange='logs', queue=self.queue_name)
        self.avgs = []
        self.desvs = []
        self.times = []
        self.start_time = double(datetime.datetime.now().timestamp())

    def printValues(self, time, avg, desv):
        self.times.append(time)
        self.avgs.append(avg)
        self.desvs.append(desv)

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

    def run(self):
        def callback(ch, method, properties, body):
            print(" [x] Received %r" % body)
            data = json.loads(body)
            time = data['time']
            self.printValues(time, [data['avg']], [data['stdev']]) # falta enviar avg y desv

        self.channel.basic_consume(queue=self.queue_name, on_message_callback=callback, auto_ack=True)
        self.channel.start_consuming()


if __name__ == '__main__':
    print('TERMINAL')
    terminal = Terminal()
    terminal.run()
