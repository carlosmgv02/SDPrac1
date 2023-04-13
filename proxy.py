import datetime

import grpc
import redis
import time
from statistics import mean, stdev

import wellnessResults
from gRPC.PROTO import terminal_pb2_grpc
from gRPC.PROTO.terminal_pb2 import WellnessResults


def strip(string):
    ls = []
    for item in string:
        ls.append(float(item.decode()[1:]))
    return ls


class Proxy:
    def __init__(self):
        self.redis_pool = redis.ConnectionPool('162.246.254.134', port=8001, db=0)
        self.redis_con = redis.Redis('162.246.254.134', port=8001, db=0)

    def getValues(self, keys):
        values = []
        for key in keys:
            values.append(self.redis_con.get(key))
        return values

    def run(self):

        window_time = 20
        window_length = 10

        while True:
            k = self.redis_con.keys()
            try:
                min_time = min(strip(k))
                date_time = datetime.datetime.fromtimestamp(min_time)
                keys = strip(k)
                values = strip(self.getValues(k))
                avg = mean(values)
                std = stdev(values)
                # Diferenciar per tipus
                wellness_results = WellnessResults(time=min_time, avg=avg, desv=std)

                # Call the retrieve_and_remove_data method every 5 seconds
                self.retrieve_and_remove_data(keys)
                # Send 2 the terminal
                channel_stub = grpc.insecure_channel('localhost:5006')
                # RRLB.set_server(channel)
                server_terminal = terminal_pb2_grpc.TerminalServiceStub(channel_stub)
                temps = date_time.strptime(str(date_time), '%Y-%m-%d %H:%M:%S')
                print(f'Sent from proxy to terminal, time: {temps}, avg: {avg}, std: {std}.')
                server_terminal.SendWellnessResults(wellness_results)
                time.sleep(window_time)
            except Exception as e:
                time.sleep(window_time)

    def retrieve_and_remove_data(self, keys):
        if keys is not None:
            for key in keys:
                return self.redis_con.flushdb()
                # Do something with the retrieved data


if __name__ == '__main__':
    print('PROXY')
    proxy = Proxy()
    proxy.run()
