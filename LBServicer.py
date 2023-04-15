from concurrent import futures
import grpc
import time
from gRPC.PROTO import meteo_utils_pb2_grpc, meteo_utils_pb2, load_balancer_pb2_grpc, load_balancer_pb2


class LoadBalancerServicer(load_balancer_pb2_grpc.LoadBalancerServicer):
    def __init__(self):
        self.server_addresses = ['localhost:5002', 'localhost:5003', 'localhost:5004']  # Hardcoded server addresses
        self.server_stubs = [grpc.insecure_channel(addr) for addr in
                             self.server_addresses]  # Create channel stubs for each server
        self.server_processors = [meteo_utils_pb2_grpc.MeteoDataServiceStub(stub) for stub in
                                  self.server_stubs]  # Create server processors for each server
        self.server_count = len(self.server_addresses)
        self.current_server = 0  # Index of the current server to use for next request

    def round_robin_server(self):
        server = self.server_processors[self.current_server]
        self.current_server = (self.current_server + 1) % self.server_count  # Update the index for the next request
        return server

    def ReceiveMeteo(self, request, context):
        print(request.time)
        done = False
        count = 0
        while not done:
            server_processor = self.round_robin_server()
            try:
                res = server_processor.ProcessMeteoData(request)
                count = 0
                done = True
            except grpc._channel._InactiveRpcError as e:
                print('Trying again')
                count += 1
            if count == len(self.server_addresses):
                print('\033[91m' + 'All servers are down' + '\033[0m')
                done = True
                exit(1)
        return load_balancer_pb2.google_dot_protobuf_dot_empty__pb2.Empty()

    def ReceivePollution(self, request, context):
        print(request.time)
        server_processor = self.round_robin_server()
        done = False
        count = 0
        try:
            res = server_processor.ProcessPollutionData(request)
            count = 0
            done = True
        except grpc._channel._InactiveRpcError as e:
            print('Trying again')
            count += 1
        if count == len(self.server_addresses):
            print('\033[91m' + 'All servers are down' + '\033[0m')
            done = True
            exit(1)
        return load_balancer_pb2.google_dot_protobuf_dot_empty__pb2.Empty()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    load_balancer_pb2_grpc.add_LoadBalancerServicerServicer_to_server(LoadBalancerServicer(), server)
    server.add_insecure_port('0.0.0.0:5000')
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    print('LOAD_BALANCER - Listening on port 5000')
    serve()
