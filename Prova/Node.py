import threading
import xmlrpc.client
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from RedisManager import RedisManager


class Node:
    def __init__(self, node_id, host, port):
        self.node_id = node_id
        self.host = host
        self.port = port
        self.redis = RedisManager(host, port)
        self.peers = []

        # Configurar el servidor XML-RPC
        self.server = SimpleXMLRPCServer((host, port),
                                         requestHandler=SimpleXMLRPCRequestHandler)
        self.server.register_introspection_functions()

        # Registrar los métodos del servicio XML-RPC
        self.server.register_function(self.add, 'add')
        self.server.register_function(self.get, 'get')
        self.server.register_function(self.delete, 'delete')

        # Iniciar el servidor en un hilo aparte
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.daemon = True
        self.server_thread.start()

    def add_peer(self, peer):
        self.peers.append(peer)

    def remove_peer(self, peer):
        self.peers.remove(peer)

    def send_message(self, peer, method, *args):
        try:
            # Crear un proxy para el nodo/servidor destino
            proxy = xmlrpc.client.ServerProxy('http://{}:{}/'.format(peer.host, peer.port))

            # Llamar al método correspondiente en el nodo/servidor destino
            result = getattr(proxy, method)(*args)

            return result
        except Exception as e:
            print('Error al enviar mensaje a {}: {}'.format(peer.node_id, e))

    def broadcast(self, method, *args):
        # Enviar un mensaje a todos los nodos/servidores del sistema distribuido
        for peer in self.peers:
            self.send_message(peer, method, *args)

    def add(self, key, value):
        self.redis.add(key, value)
        self.broadcast('add', key, value)

    def get(self, key):
        return self.redis.get(key)

    def delete(self, key):
        result = self.redis.delete(key)
        if result:
            self.broadcast('delete', key)
            return True
        else:
            return False
