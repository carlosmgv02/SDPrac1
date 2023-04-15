import datetime
import time

import grpc
from numpy import double

import meteo_utils
from gRPC.PROTO import load_balancer_pb2_grpc, load_balancer_pb2
from gRPC.PROTO.meteo_utils_pb2 import AirAnalysisResponse

channel = grpc.insecure_channel('localhost:5000')
print('Sensor - running on 50050')
# create a stub (client)
stub = load_balancer_pb2_grpc.LoadBalancerServicerStub(channel)

# create a valid request message
empty = load_balancer_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
meteo_data = meteo_utils.MeteoDataDetector()

while True:
    meteoRes = meteo_data.analyze_air()
    meteoReq = AirAnalysisResponse(temperature=meteoRes["temperature"], humidity=meteoRes["humidity"])
    meteoReq.time = 0
    currTime = datetime.datetime.timestamp(datetime.datetime.now())
    print('Calculated time: ', currTime)
    meteoReq.time = double(currTime)
    print('Request time: ', meteoReq.time)
    print('METEO_TIME: ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print('Temperature: ', meteoReq.temperature, 'Humidity: ', meteoReq.humidity, 'Time: ', meteoReq.time)
    stub.ReceiveMeteo(meteoReq)
    time.sleep(1)

