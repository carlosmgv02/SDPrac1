import grpc
import random


class RoundRobinLoadBalancer:
    def __init__(self, addresses):
        self.addresses = addresses
        self.current_index = 0

    def get_next_address(self):
        address = self.addresses[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.addresses)
        return address


class GreeterClient:
    def __init__(self, addresses):
        self.load_balancer = RoundRobinLoadBalancer(addresses)
        self.channel = grpc.insecure_channel(self.load_balancer.get_next_address())

    def greet(self, name):
        stub = greeter_pb2_grpc.GreeterStub(self.channel)
        response = stub.SayHello(greeter_pb2.HelloRequest(name=name))
        return response.message

        # use the load balancer to get the next available address
        self.channel = grpc.insecure_channel(self.load_balancer.get_next_address())


addresses = ["localhost:50051", "localhost:50052", "localhost:50053"]
client = GreeterClient(addresses)

# Call greet() on the client multiple times and see that it connects to different servers in round-robin fashion.
for i in range(5):
    name = input("What's your name? ")
    response = client.greet(name)
    print(response)
