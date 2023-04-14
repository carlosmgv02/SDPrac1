import datetime
import time

from jsonpickle import json
import pika
from numpy import double

import meteo_utils


def analyzePollution():
    detector = meteo_utils.MeteoDataDetector()
    meteo_data = detector.analyze_pollution()
    meteo_data['timestamp'] = double(datetime.datetime.timestamp(datetime.datetime.now()))
    return meteo_data


connection = pika.BlockingConnection(pika.ConnectionParameters('162.246.254.134'))
channel = connection.channel()

print('METEO_SENSOR')

while True:
    messages = [analyzePollution()]
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
