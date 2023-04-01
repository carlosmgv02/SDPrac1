import sys
import xmlrpc.server
import redis

# Obtener los argumentos de línea de comando
if len(sys.argv) != 2:
    print("Uso: nodo.py <puerto>")
    sys.exit(1)
port = 9000

# Crear la conexión con la base de datos Redis
redis_client = redis.Redis(host='162.246.254.134', port=8001)


# Crear el nodo que recibe y guarda la información en Redis
class Node(xmlrpc.server.SimpleXMLRPCServer):
    def receive_info(self, data):
        self.process_pollution(data["temperature"], data["humidity"])
        self.process_air(data["co2"])

    def process_pollution(self, temp, hum):
        self.temp = temp
        self.hum = hum

    def process_air(self, co2):
        self.co2 = co2


# Iniciar el servidor XMLRPC del nodo en el puerto especificado
node = Node('localhost', port)

print('Nodo iniciado en el puerto {}'.format(port))
node.register_function(node.receive_info, 'send_info')
node.serve_forever()
