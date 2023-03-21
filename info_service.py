import redis


class InfoService:

    def __init__(self):
        self.users = redis.Redis('162.246.254.134', port=8001, db=0, decode_responses=True, )

    def add_user(self, username, name):
        print('User received:\n\tUsername: ' + username + '\n\tName: ' + name)
        self.users.set(username, name)
        return 'Done'

    def get_users(self):
        insults = []
        keys = self.users.keys()
        for key in keys:
            insults.append(key + ': ' + self.users.get(key))
        return list(insults)

    def get_user(self, username):
        return self.users.get(username)

    def delete_user(self, username):
        print('User to delete: ' + username)
        self.users.delete(username)
        return 'Done'

    def bondia(self):
        print('vondia')
        return "vondia"

    def publish(self, topic, message):
        print('Publishing message: ' + message + ' to topic: ' + topic)
        self.users.publish(topic, message)
        return 'Done'

    def subscribe(self, topic):
        print('Subscribing to topic: ' + topic)
        pubsub = self.users.pubsub()
        pubsub.subscribe(topic)
        while True:
            message = pubsub.get_message()
            print(message)
        if message:
            print('Received message: ' + str(message['data']))


info_service = InfoService()
