import redis


class InfoService:

    def __init__(self):
        self.users = redis.Redis('localhost', port=6379, db=0, decode_responses=True)

    def add_user(self, username, name):
        print('User received:\n\tUsername: ' + username + '\n\tName: ' + name)
        return 'Done'

    def get_users(self):
        insults = []
        keys = self.users.keys()
        for key in keys:
            insults.append(key + ': ' + self.users.get(key))
        return list(insults)

    def get_user(self, username):
        print(self.users.get(username))

    def delete(self, username):
        self.get_users.delete(username)


info_service = InfoService()
