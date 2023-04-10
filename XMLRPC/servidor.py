from client import meteo_data, pollution_data
from meteo_utils import MeteoDataProcessor
from dataInstance import MeteoData
from pollutionData import PollutionData


processor = MeteoDataProcessor()
meteo_data = MeteoData(meteo_data["temperature"], meteo_data["humidity"])
wellness_data = processor.process_meteo_data(meteo_data)
pollution_data = PollutionData(pollution_data["co2"])
pollution_data_processed = processor.process_pollution_data(pollution_data)
# process_meteo_data expects RawMeteoData: an object
# with the attributes temperature and humidity
# process_pollution_data expects RawPollutionData: an object
# with the attribute co2

# sensors>load_balancer>servidors que fan calcul>redis
# meteo_data = sensor.analyze_air()

