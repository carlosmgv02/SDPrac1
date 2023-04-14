import datetime


class MeteoData:
    def __init__(self, temperature, humidity, timestamp):
        self.temperature = temperature
        self.humidity = humidity
        self.timestamp = timestamp

    def to_dict(self):
        return {
            "temperature": self.temperature,
            "humidity": self.humidity,
            "timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        }


class PollutionData:
    def __init__(self, co2, timestamp):
        self.co2 = co2
        self.timestamp = timestamp

    def to_dict(self):
        return {
            "co2": self.co2,
            "timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        }


class DataCalculus:
    def __init__(self, time, avg, stdev, type):
        self.time = time
        self.average = avg
        self.stdev = stdev
        self.type = type

    def to_dict(self):
        return {
            "time": self.time.strftime("%Y-%m-%d %H:%M:%S"),
            "average": self.average
        }
