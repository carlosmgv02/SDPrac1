import grpc
import meteo_utils_pb2
import meteo_utils_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:5001')

# create a stub (client)
stub = meteo_utils_pb2_grpc.MeteoDataServiceStub(channel)

# create a valid request message
empty = meteo_utils_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
response = stub.AnalyzeAir(empty)

# print the response
print(response.temperature)
print(response.humidity)

# create a valid request message
# pollution_data = meteo_utils_pb2.PollutionData(co2=1000)
empty = meteo_utils_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
response = stub.AnalyzePollution(empty)

# print the response
print(response.co2)
