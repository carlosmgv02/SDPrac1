
class MeteoData:
    def __init__(self, temperature, humidity, timestamp):
        self.temperature = temperature
        self.humidity = humidity
        self.timestamp = timestamp

    def __str__(self):
        return "Temperature: " + str(self.temperature) + " Humidity: " + str(self.humidity) + " Timestamp: " + str(self.timestamp)
