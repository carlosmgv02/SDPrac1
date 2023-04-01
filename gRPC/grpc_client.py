import meteo_utils

import grpc

# import the generated classes
#import insultingServer_pb2
#import insultingServer_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = insultingServer_pb2_grpc.InsultingServiceStub(channel)




conn = xmlrpc.client.ServerProxy('http://localhost:9000')
detector = meteo_utils.MeteoDataDetector()

# Air sensors
meteo_data = detector.analyze_air()
conn.send_info(meteo_data)
# returns a dictionary; { “temperature”: x, “humidity”: y }
# Pollution sensors
pollution_data = detector.analyze_pollution()
# returns a dictionary; { “co2”: z }
print(meteo_data)
print(pollution_data)

proxy = xmlrpc.client.ServerProxy('http://localhost:4000/')
