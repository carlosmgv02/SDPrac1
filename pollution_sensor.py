import datetime
import time

import grpc
from numpy import double

import meteo_utils
from gRPC.PROTO import load_balancer_pb2_grpc, load_balancer_pb2
from gRPC.PROTO.meteo_utils_pb2 import PollutionAnalysisResponse, AirAnalysisResponse

channel = grpc.insecure_channel('localhost:5000')
print('Sensor - running on 50050')

# create a stub (client)
stub = load_balancer_pb2_grpc.LoadBalancerServicerStub(channel)

# create a valid request message
empty = load_balancer_pb2.google_dot_protobuf_dot_empty__pb2.Empty()

meteo_data = meteo_utils.MeteoDataDetector()
while True:
    meteo_res = meteo_data.analyze_pollution()
    pollutionReq = PollutionAnalysisResponse(co2=meteo_res["co2"])
    pollutionReq.time = 0
    currTime = datetime.datetime.timestamp(datetime.datetime.now())
    print('Calculated time: ', currTime)
    pollutionReq.time = double(currTime)
    print('POLL_TIME: '+ datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    stub.ReceivePollution(pollutionReq)
    # print the response
    print('pollutionReq: ', pollutionReq)
    print(pollutionReq)
    time.sleep(1)

