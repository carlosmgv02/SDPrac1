import datetime

import grpc
from gRPC.PROTO import load_balancer_pb2
from gRPC.PROTO import load_balancer_pb2_grpc
import sys


# open a gRPC channel
channel = grpc.insecure_channel('localhost:5000')
print('running on 50050' )

# create a stub (client)
stub = load_balancer_pb2_grpc.LoadBalancerServicerStub(channel)

# create a valid request message
empty = load_balancer_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
meteoReq = stub.AnalyzeAir(empty)
meteoReq.time = float(datetime.datetime.now().timestamp())
stub.ReceiveMeteo(meteoReq)
print('meteoReq: ')
print(meteoReq)

# create a valid request message
# pollution_data = meteo_utils_pb2.PollutionData(co2=1000)
empty = load_balancer_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
pollutionReq = stub.AnalyzePollution(empty)
pollutionReq.time = float(datetime.datetime.now().timestamp())
stub.ReceivePollution(pollutionReq)
# print the response
print('pollutionReq: ')
print(pollutionReq)


