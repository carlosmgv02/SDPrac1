import meteo_utils
import xmlrpc.client
import xmlrpc.client

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
