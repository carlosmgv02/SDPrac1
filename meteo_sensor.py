import datetime

import grpc
import pika
from jsonpickle import json
from numpy import double

import meteo_utils
import time


def analyzeAir():
    detector = meteo_utils.MeteoDataDetector()
    meteo_data = detector.analyze_air()
    meteo_data['timestamp'] = double(datetime.datetime.now().timestamp())
    return meteo_data


channel = grpc.insecure_channel('localhost:5000')
connection = pika.BlockingConnection(pika.ConnectionParameters('162.246.254.134'))
channel = connection.channel()

print('SENSOR')

while True:
    messages = [analyzeAir()]
    for message in messages:
        channel.basic_publish(
            exchange='',
            routing_key='client-server',
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=2)  # make message persistent
        )
        print(" [x] Sent %r" % message)
    time.sleep(1)
