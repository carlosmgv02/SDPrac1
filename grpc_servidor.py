import grpc
from concurrent import futures
import time

import meteo_utils
from meteo_utils import MeteoDataProcessor
from meteoData import MeteoData
from pollutionData import PollutionData

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
        detector = meteo_utils.MeteoDataDetector()
        meteo_data = detector.analyze_air()
        print(meteo_data)
        #temperature=20.0, humidity=3.0
        response = meteo_utils_pb2.AirAnalysisResponse(meteo_data)
        return response

    def AnalyzePollution(self, request, context):
        # Here you can write your implementation to analyze the pollution level
        # For example, let's say you want to return some dummy data
        detector = meteo_utils.MeteoDataDetector()
        meteo_data = detector.analyze_pollution()
        response = meteo_utils_pb2.PollutionAnalysisResponse(co2=334400.0)
        return response


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
meteo_utils_pb2_grpc.add_MeteoDataServiceServicer_to_server(MeteoDataServiceServicer(), server)
print('Starting server. Listening on port 50051.')

server.add_insecure_port('[::]:5001')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
