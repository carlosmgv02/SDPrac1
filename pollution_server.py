import grpc
from concurrent import futures
import time

import meteo_utils

from gRPC.PROTO import meteo_utils_pb2_grpc, meteo_utils_pb2


class PollutionServiceServicer(meteo_utils_pb2_grpc.MeteoDataServiceServicer):

    def ProcessPollutionData(self, request, context):
        # Here you can write your implementation to process pollution data from the request
        # For example, let's say you want to calculate the co2 wellness index based on the given co2 value
        co2 = request.co2

        # Perform some calculations to calculate the wellness index
        wellness_index = 100 - co2

        # Create and return the response object
        response = meteo_utils_pb2.Co2Wellness(wellness=wellness_index)
        return response



# Use a RoundRobinLoadBalancer instead of a list of addresses
# load_balancer = RoundRobinLoadBalancer(["localhost:5001", "localhost:5002", "localhost:5003"])

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
meteo_utils_pb2_grpc.add_MeteoDataServiceServicer_to_server(PollutionServiceServicer(), server)

print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:5001')

server.start()
# print(load_balancer.get_next_address())

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
