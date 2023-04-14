import datetime
import json

import pika
import redis
import time
from statistics import mean, stdev

from numpy import double

from dataInstance import DataCalculus


def strip(string):
    ls = []
    for item in string:
        ls.append(double(item.decode()[1:]))
    return ls


class Proxy:
    def __init__(self):
        self.redis_pool = redis.ConnectionPool('162.246.254.134', port=8001, db=0)
        self.redis_con = redis.Redis('162.246.254.134', port=8001, db=0)
        self.channel = pika.BlockingConnection(pika.ConnectionParameters('162.246.254.134')).channel()
        self.channel.queue_declare(queue='')
        self.channel.exchange_declare(exchange='logs', exchange_type='fanout')

    def getValues(self, keys):
        values = []
        for key in keys:
            values.append(self.redis_con.get(key).decode())

        return values

    def getPollutionValues(self, keys):
        key_list = []
        for key in keys:
            if key.decode()[0] == 'p':
                key_list.append(key)
        return self.getValues(key_list)

    def getMeteoValues(self, keys):
        key_list = []
        for key in keys:
            if key.decode()[0] == 'm':
                key_list.append(key)
        return self.getValues(key_list)

    def getDataCalculus(self, type):
        keys = self.redis_con.keys()
        if type == 'pollution':
            values = self.getPollutionValues(keys)
        else:
            values = self.getMeteoValues(keys)
        date_time = datetime.datetime.fromtimestamp(min(strip(self.redis_con.keys())))
        avg = mean(values)
        std = stdev(values)
        print(f'{type.upper()} -> avg: {avg}, stdev: {std}')
        return DataCalculus(date_time, avg, std, type=type)

    def run(self):

        window_time = 10
        window_length = 10

        while True:
            k = self.redis_con.keys()
            try:
                min_time = min(strip(k))
                date_time = datetime.datetime.fromtimestamp(min_time)
                keys = strip(k)
                meteo = self.getDataCalculus('meteo').to_dict()
                pollution = self.getDataCalculus('pollution').to_dict()

                self.channel.basic_publish(exchange='logs', routing_key='', body=meteo)
                self.channel.basic_publish(exchange='logs', routing_key='', body=pollution)
                print(" [x] Sent %r" % meteo)
                print(" [x] Sent %r" % pollution)
                # Call the retrieve_and_remove_data method every 5 seconds
                print(self.retrieve_and_remove_data(keys))
                time.sleep(window_time)
            except ValueError:
                print(ValueError)
                time.sleep(window_time)

    def retrieve_and_remove_data(self, keys):
        if keys is not None:
            for key in keys:
                return self.redis_con.flushdb()
                # Do something with the retrieved data

    def SendWellnessResults(self, request, context):
        return


if __name__ == '__main__':
    print('PROXY')
    proxy = Proxy()
    proxy.run()
