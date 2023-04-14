import datetime
import time

import grpc

from gRPC.PROTO import load_balancer_pb2
from gRPC.PROTO import load_balancer_pb2_grpc
import sys
import meteo_utils
from gRPC.PROTO.load_balancer_pb2 import AirAnalysisResponse, PollutionAnalysisResponse

# open a gRPC channel
channel = grpc.insecure_channel('localhost:5000')
print('Sensor - running on 50050')

# create a stub (client)
stub = load_balancer_pb2_grpc.LoadBalancerServicerStub(channel)

# create a valid request message
empty = load_balancer_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
while True:
    meteo_data = meteo_utils.MeteoDataDetector()
    meteoRes = meteo_data.analyze_air()
    meteoReq = AirAnalysisResponse(temperature=meteoRes["temperature"], humidity=meteoRes["humidity"])
    meteoReq.time = float(datetime.datetime.now().timestamp())
    print('METEO_TIME: '+ datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print('Temperature: ', meteoReq.temperature, 'Humidity: ', meteoReq.humidity, 'Time: ', meteoReq.time)
    stub.ReceiveMeteo(meteoReq)
    print('meteoReq: ', meteoReq)
    meteo_res = meteo_data.analyze_pollution()
    pollutionReq = PollutionAnalysisResponse(co2=meteo_res["co2"])
    pollutionReq.time = float(datetime.datetime.now().timestamp())
    print('POLL_TIME: '+ datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    stub.ReceivePollution(pollutionReq)
    # print the response
    print('pollutionReq: ', pollutionReq)
    print(pollutionReq)
# create a valid request message
# pollution_data = meteo_utils_pb2.PollutionData(co2=1000)
# empty = load_balancer_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
#
# while True:
#     pollutionReq = stub.AnalyzePollution(empty)
#     pollutionReq.time = float(datetime.datetime.now().timestamp())
#     stub.ReceivePollution(pollutionReq)
#     time.sleep(2)
# # print the response
# print('pollutionReq: ')
# print(pollutionReq)


