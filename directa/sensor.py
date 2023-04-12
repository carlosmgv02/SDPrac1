import datetime

import grpc
import pika
from jsonpickle import json

import meteo_utils
import time

def analyzeAir():
    detector = meteo_utils.MeteoDataDetector()
    meteo_data = detector.analyze_air()
    meteo_data['timestamp'] = float(datetime.datetime.now().timestamp())
    return meteo_data


def analyzePollution():
    detector = meteo_utils.MeteoDataDetector()
    meteo_data = detector.analyze_pollution()
    meteo_data['timestamp'] = float(datetime.datetime.now().timestamp())
    return meteo_data


channel = grpc.insecure_channel('localhost:5000')
connection = pika.BlockingConnection(pika.ConnectionParameters('162.246.254.134'))
channel = connection.channel()

print('Sensor - running on 50050')
while True:
    messages =[]
    messages.append(analyzeAir())
    messages.append(analyzePollution())
    for message in messages:
        channel.basic_publish(
            exchange='',
            routing_key='client-server',
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=2)  # make message persistent
        )
        print(" [x] Sent %r" % message)
    time.sleep(2)
