import os
import sys

import grpc
from concurrent import futures
import time

import pika
import redis
import meteo_utils
from dataInstance import MeteoData
from dataInstance import PollutionData
from gRPC.PROTO import meteo_utils_pb2_grpc, meteo_utils_pb2

from loadBalancer import RRLB
import json


class MeteoDataServiceServicer():

    def __init__(self):
        self.meteo_data_processor = meteo_utils.MeteoDataProcessor()
        self.redisClient = redis.Redis('162.246.254.134', port=8001)
        self.channel = pika.BlockingConnection(pika.ConnectionParameters('162.246.254.134')).channel()

    def process_meteo(self, data):
        meteo_data = MeteoData(data['temperature'], data['humidity'], data['timestamp'])
        return self.meteo_data_processor.process_meteo_data(meteo_data)

    def process_pollution(self, data):
        pollution_data = PollutionData(data['co2'], data['timestamp'])
        return self.meteo_data_processor.process_pollution_data(pollution_data)

    def saveData(self, data):
        data = json.loads(data)
        if 'co2' in data:
            res = self.process_pollution(data)
        else:
            res = self.process_meteo(data)
        timestamp = data['timestamp']
        return self.redisClient.set(f'm{str(timestamp)}', str(res).encode('utf-8'))

    def processData(self):
        def callback(ch, method, properties, body):
            print(" [x] Received %r" % body.decode())
            time.sleep(body.count(b'.'))
            print(" [x] Done")
            ch.basic_ack(delivery_tag=method.delivery_tag)
            self.saveData(body)

        self.channel.basic_consume(
            queue='client-server',
            on_message_callback=callback)
        self.channel.basic_qos(prefetch_count=1)

        self.channel.start_consuming()


print('METEO_SERVER - Listening on port. polls')
if __name__ == '__main__':
    try:
        while True:
            server = MeteoDataServiceServicer()
            server.processData()
            time.sleep(86400)
    except KeyboardInterrupt:

        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
