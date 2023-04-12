import redis
import time
from statistics import mean, stdev


class Proxy:
    def __init__(self):
        self.redis_pool = redis.ConnectionPool('162.246.254.134', port=8001, db=0)
        self.redis_con = redis.Redis('162.246.254.134', port=8001, db=0)

    def strip(self, string):
        ls = []
        for item in string:
            ls.append(float(item.decode()[1:]))
        return ls
    def delete_until_first_number(self, string):
        index = 0
        for i, char in enumerate(string):
            if char.isdigit():
                index = i
                break
        return string[index:]

    def run(self):

        window_time = 10
        window_length = 10


        while True:
            k = self.redis_con.keys()
            keys = self.strip(k)
            avg = mean(keys)
            std = stdev(keys)
            print(f'avg: {avg}, stdev: {std}')
            # Call the retrieve_and_remove_data method every 5 seconds
            print(self.retrieve_and_remove_data(keys))
            time.sleep(window_time)

    def retrieve_and_remove_data(self, keys):
        if keys is not None:
            for key in keys:
                return self.redis_con.flushdb()
                # Do something with the retrieved data

    def SendWellnessResults(self, request, context):
        return


if __name__ == '__main__':
    proxy = Proxy()
    proxy.run()
