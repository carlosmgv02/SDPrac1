import grpc
import meteo_utils_pb2
import meteo_utils_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = meteo_utils_pb2_grpc.MeteoDataServiceStub(channel)

# create a valid request message
meteo_data = meteo_utils_pb2.MeteoData(temperature=25.5, humidity=50.0)
response = stub.ProcessMeteoData(meteo_data)

# print the response
print(response.wellness_data.temperature)
print(response.wellness_data.humidity)

# create a valid request message
pollution_data = meteo_utils_pb2.PollutionData(co2=1000)
response = stub.ProcessPollutionData(pollution_data)

# print the response
print(response.pollution_data_processed.co2)

# create a valid request message
air_data = meteo_utils_pb2.AirData(temperature=25.5, humidity=50.0, co2=1000)
response = stub.AnalyzeAir(air_data)

# print the response
print(response.wellness_data.temperature)
print(response.wellness_data.humidity)
print(response.pollution_data_processed.co2)

# create a valid request message
pollution_data = meteo_utils_pb2.PollutionData(co2=1000)
response = stub.AnalyzePollution(pollution_data)

# print the response
print(response.pollution_data_processed.co2)