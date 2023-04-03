import grpc
from concurrent import futures
import time

import meteo_utils_pb2
import meteo_utils_pb2_grpc


class MeteoDataServiceServicer(meteo_utils_pb2_grpc.MeteoDataServiceServicer):
    def ProcessMeteoData(self, request, context):
        # Here you can write your implementation to process meteo data from the request
        # For example, let's say you want to calculate the air wellness index based on the given parameters
        temperature = request.temperature
        co2 = request.co2
        humidity = request.humidity

        # Perform some calculations to calculate the wellness index
        wellness_index = (temperature + humidity) / (2 * co2)

        # Create and return the response object
        response = meteo_utils_pb2.AirWellness(wellness=wellness_index)
        return response

    def ProcessPollutionData(self, request, context):
        # Here you can write your implementation to process pollution data from the request
        # For example, let's say you want to calculate the co2 wellness index based on the given co2 value
        co2 = request.co2

        # Perform some calculations to calculate the wellness index
        wellness_index = 100 - co2

        # Create and return the response object
        response = meteo_utils_pb2.Co2Wellness(wellness=wellness_index)
        return response

    def AnalyzeAir(self, request, context):
        # Here you can write your implementation to analyze the air quality
        # For example, let's say you want to return some dummy data
        response = meteo_utils_pb2.AirAnalysisResponse(temperature=25.0, humidity=50.0)
        return response

    def AnalyzePollution(self, request, context):
        # Here you can write your implementation to analyze the pollution level
        # For example, let's say you want to return some dummy data
        response = meteo_utils_pb2.PollutionAnalysisResponse(co2=500.0)
        return response


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
meteo_utils_pb2_grpc.add_MeteoDataServiceServicer_to_server(MeteoDataServiceServicer(), server)
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)

#processor = MeteoDataProcessor()
#meteo_data = MeteoData(meteo_data["temperature"], meteo_data["humidity"])
#wellness_data = processor.process_meteo_data(meteo_data)
#pollution_data = PollutionData(pollution_data["co2"])
#pollution_data_processed = processor.process_pollution_data(pollution_data)
# process_meteo_data expects RawMeteoData: an object
# with the attributes temperature and humidity
# process_pollution_data expects RawPollutionData: an object
# with the attribute co2

# sensors>load_balancer>servidors que fan calcul>redis
# meteo_data = sensor.analyze_air()
