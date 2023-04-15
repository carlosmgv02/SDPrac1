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
        self.last_timestamp = datetime.datetime.now()
    def getValues(self, keys):
        values = []
        for key in keys:
            values.append(float(self.redis_con.get(key).decode()))
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

    def getDataCalculus(self, tipo, min_time):
        keys = self.redis_con.keys()
        # if tipo == 'pollution':
        #    values = self.getPollutionValues(keys)
        #else:
        #    values = self.getMeteoValues(keys)
        values = self.getValues(keys)
        date_time = min(strip(self.redis_con.keys()))
        avg = mean(values)
        std = stdev(values)
        print(f'{tipo.upper()} -> avg: {avg}, stdev: {std}')
        return DataCalculus(min_time, avg, std, tipo=tipo)

    def run(self):

        window_time = 10
        window_length = 10
        while True:
            current_time = datetime.datetime.now()
            time_diff = (current_time - self.last_timestamp).total_seconds()
            try:
                if time_diff >= window_time:
                    k = self.redis_con.keys()
                    if k:
                        min_time = min(strip(k))+window_time
                        keys = strip(k)
                        meteo = self.getDataCalculus('meteo', min_time).__dict__()
                        # pollution = self.getDataCalculus('pollution', min_time).__dict__()
                        self.channel.basic_publish(exchange='logs', routing_key='', body=json.dumps(meteo))
                        # self.channel.basic_publish(exchange='logs', routing_key='', body=json.dumps(pollution))
                        print(" [x] Sent %r" % meteo)
                        # print(" [x] Sent %r" % pollution)
                        # Call the retrieve_and_remove_data method every 5 seconds
                        print(self.retrieve_and_remove_data(keys))
                    self.last_timestamp = current_time
                time.sleep(window_time)
            except ValueError:
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
