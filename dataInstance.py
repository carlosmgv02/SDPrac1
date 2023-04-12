class MeteoData:
    def __init__(self, temperature, humidity, timestamp):
        self.temperature = temperature
        self.humidity = humidity
        self.timestamp = timestamp

    def __str__(self):
        return "Temperature: " + str(self.temperature) + " Humidity: " + str(self.humidity) + " Timestamp: " + str(
            self.timestamp)


class PollutionData:
    def __init__(self, co2, timestamp):
        self.co2 = co2
        self.timestamp = timestamp

    def __str__(self):
        return "CO2: " + str(self.co2) + " Timestamp: " + str(self.timestamp)


class DataCalculus:
    def __init__(self, time, average, stdev):
        self.time = time
        self.average = average
        self.stdev = stdev

    def __str__(self):
        return "Time: " + str(self.time) + " Average: " + str(self.average) + " Stdev: " + str(self.stdev)
