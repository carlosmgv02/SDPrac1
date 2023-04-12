import grpc
import redis
import time
from statistics import mean, stdev

import wellnessResults
from gRPC.PROTO import terminal_pb2_grpc
from wellnessResults import WellnessResults


class Proxy:
    def __init__(self):
        self.redis_pool = redis.ConnectionPool('162.246.254.134', port=8001, db=0)
        self.redis_con = redis.Redis('162.246.254.134', port=8001, db=0)

    def strip(self, string):
        ls = []
        for item in string:
            ls.append(float(item.decode()[1:]))
        return ls

    def run(self):

        window_time = 20
        window_length = 10

        while True:
            k = self.redis_con.keys()
            keys = self.strip(k)
            if len(keys) > 1:
                avg = mean(keys)
                std = stdev(keys)
                # Diferenciar per tipus
                wellness_results = WellnessResults(avg, std)
                print(f'WR: {wellness_results}')
                # Call the retrieve_and_remove_data method every 5 seconds
                print(self.retrieve_and_remove_data(keys))
                # Send 2 the terminal
                channel_stub = grpc.insecure_channel('localhost:5006')
                # RRLB.set_server(channel)
                server_terminal = terminal_pb2_grpc.TerminalServiceStub(channel_stub)
                print('this is the response')
                server_terminal.SendWellnessResults(server_terminal)
                time.sleep(window_time)

    def retrieve_and_remove_data(self, keys):
        if keys is not None:
            for key in keys:
                return self.redis_con.flushdb()
                # Do something with the retrieved data


if __name__ == '__main__':
    proxy = Proxy()
    proxy.run()
