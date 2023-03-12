import redis


class RedisManager:
    def __init__(self, host='localhost', port=6379, db=0):
        self.r = redis.Redis(host, port=port, db=db, decode_responses=True)

    def add(self, key, value):
        res = self.r.set(key, value)
        return 'Done'

    def get(self, key):
        return self.r.get(key)

    def delete(self, key):
        result = self.r.delete(key)
        if result:
            return True
        else:
            return False
