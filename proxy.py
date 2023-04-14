import datetime
import grpc
import redis
import time
from statistics import mean, stdev

from numpy import double

from gRPC.PROTO import terminal_pb2_grpc
from gRPC.PROTO.terminal_pb2 import WellnessResults


def strip(string):
    ls = []
    for item in string:
        ls.append(double(item.decode()[1:]))
    return ls

class Proxy:
    def __init__(self):
        self.redis_pool = redis.ConnectionPool('162.246.254.134', port=8001, db=0)
        self.redis_con = redis.Redis('162.246.254.134', port=8001, db=0)
        self.window_time = 10
        self.window_length = 10
        self.last_timestamp = datetime.datetime.now()

    def get_values(self, keys):
        values = []
        for key in keys:
            values.append(float(self.redis_con.get(key)))
        return values

    def run(self):
        while True:
            current_time = datetime.datetime.now()
            time_diff = (current_time - self.last_timestamp).total_seconds()
            if time_diff >= self.window_time:
                keys = self.redis_con.keys()
                if keys:
                    values = self.get_values(keys)
                    avg = mean(values)
                    std = stdev(values)
                    min_time = min(strip(keys))+self.window_time
                    print('MIN_TIME: '+str(min_time))
                    wellness_results = WellnessResults(time=min_time, avg=avg, desv=std)
                    channel_stub = grpc.insecure_channel('localhost:5006')
                    server_terminal = terminal_pb2_grpc.TerminalServiceStub(channel_stub)
                    print(f'Sent from proxy to terminal, time: {wellness_results.time}, avg: {avg}, std: {std}.')
                    server_terminal.SendWellnessResults(wellness_results)
                    self.redis_con.flushdb()
                self.last_timestamp = current_time
            time.sleep(self.window_time)

if __name__ == '__main__':
    print('PROXY')
    proxy = Proxy()
    proxy.run()
