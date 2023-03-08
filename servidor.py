import redis
from xmlrpc.server import SimpleXMLRPCServer
import logging
from info_service import info_service
from concurrent import futures

logging.basicConfig(level=logging.INFO)
print('*******BENVINGUT AL PROGRAMA*******')
server = SimpleXMLRPCServer(("localhost", 4000))

logging.basicConfig(level=logging.INFO)


server.register_instance(info_service)

# server.register_function(info_service)

try:
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting')
