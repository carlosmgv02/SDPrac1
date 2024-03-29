import sys

import grpc
from concurrent import futures
import time
import redis
from numpy import double

import meteo_utils
from dataInstance import MeteoData
from dataInstance import PollutionData
from gRPC.PROTO import meteo_utils_pb2_grpc, meteo_utils_pb2
import datetime
import json


class MeteoDataServiceServicer(meteo_utils_pb2_grpc.MeteoDataServiceServicer):

    def __init__(self):
        self.meteo_data_processor = meteo_utils.MeteoDataProcessor()
        self.redisClient = redis.Redis('162.246.254.134', port=8001)

    def get_all_meteo_data(self):
        all_data = {}
        for key in self.redisClient.keys():
            data = self.redisClient.hgetall(key)
            meteo_data = MeteoData(float(data[b'temperature']), float(data[b'humidity']), double(data[b'timestamp']))
            all_data[key] = meteo_data
        return all_data

    def ProcessMeteoData(self, request, context):
        # Here you can write your implementation to process meteo data from the request
        # For example, let's say you want to calculate the air wellness index based on the given parameters
        print("the req" + str(request))
        meteo_data = MeteoData(request.temperature, request.humidity, request.time)
        serialized_meteo_data = meteo_data.__dict__
        wellness = self.meteo_data_processor.process_meteo_data(request)
        print('POLL_TIME: '+ datetime.datetime.fromtimestamp(request.time).strftime('%Y-%m-%d %H:%M:%S'))

        print(self.redisClient.set(f'm{str(request.time)}', str(wellness).encode('utf-8')))

        response = meteo_utils_pb2.Co2Wellness(wellness=wellness)

        return response

    def ProcessPollutionData(self, request, context):
        # Here you can write your implementation to process meteo data from the request
        # For example, let's say you want to calculate the air wellness index based on the given parameters
        print("Pollution request: " + str(request))
        meteo_data = PollutionData(request.co2, request.time)
        serialized_meteo_data = meteo_data.__dict__
        wellness = self.meteo_data_processor.process_pollution_data(request)
        print(self.redisClient.set(f'p{str(request.time)}', str(wellness).encode('utf-8')))

        response = meteo_utils_pb2.Co2Wellness(wellness=wellness)


        return response


# Use a RoundRobinLoadBalancer instead of a list of addresses
# load_balancer = RoundRobinLoadBalancer(["localhost:5001", "localhost:5002", "localhost:5003"])

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
meteo_utils_pb2_grpc.add_MeteoDataServiceServicer_to_server(MeteoDataServiceServicer(), server)

# port = RRLB.get_server()

print('METEO_SERVER - Listening on port.')
port = sys.argv[1]
print('0.0.0.0'+port)
server.add_insecure_port('0.0.0.0:'+port)

server.start()
# print(load_balancer.get_next_address())

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
