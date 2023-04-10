import grpc
from concurrent import futures
import time

import redis

import meteo_utils
from dataInstance import PollutionData

from gRPC.PROTO import meteo_utils_pb2_grpc, meteo_utils_pb2, proxy_pb2_grpc


class PollutionServiceServicer(meteo_utils_pb2_grpc.MeteoDataServiceServicer):

    def __init__(self):
        self.meteo_data_processor = meteo_utils.MeteoDataProcessor()
        self.redisClient = redis.Redis('162.246.254.134', port=8001)

    def ProcessPollutionData(self, request, context):
        # Here you can write your implementation to process meteo data from the request
        # For example, let's say you want to calculate the air wellness index based on the given parameters
        print("Pollution request: " + str(request))
        meteo_data = PollutionData(request.co2, request.time)
        serialized_meteo_data = meteo_data.__dict__
        wellness = self.meteo_data_processor.process_pollution_data(request)
        print(self.redisClient.set(str(request.time), wellness))

        response = meteo_utils_pb2.Co2Wellness(wellness=wellness)

        channel_proxy = grpc.insecure_channel('localhost:5004')
        # RRLB.set_server(channel)
        server_processor = proxy_pb2_grpc.ProxyServicerStub(channel_proxy)
        print('this is the response sending to the proxy')
        res = server_processor.GetPollution(request)

        return response


# Use a RoundRobinLoadBalancer instead of a list of addresses
# load_balancer = RoundRobinLoadBalancer(["localhost:5001", "localhost:5002", "localhost:5003"])

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
meteo_utils_pb2_grpc.add_MeteoDataServiceServicer_to_server(PollutionServiceServicer(), server)

print('Starting server. Listening on port 50033.')
server.add_insecure_port('0.0.0.0:5003')

server.start()
# print(load_balancer.get_next_address())

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
