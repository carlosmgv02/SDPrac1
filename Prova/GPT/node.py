import sys
import xmlrpc.server
import redis

# Obtener los argumentos de línea de comando
if len(sys.argv) != 2:
    print("Uso: nodo.py <puerto>")
    sys.exit(1)
puerto = int(sys.argv[1])

# Crear la conexión con la base de datos Redis
redis_client = redis.Redis(host='162.246.254.134', port=8001)


# Crear el nodo que recibe y guarda la información en Redis
class Nodo(xmlrpc.server.SimpleXMLRPCServer):
    def recibir_informacion(self, informacion):
        # Guardar la información en Redis
        redis_client.set('informacion', informacion)
        return 'Informacion recibida'


# Iniciar el servidor XMLRPC del nodo en el puerto especificado
nodo = Nodo(('localhost', puerto))

print('Nodo iniciado en el puerto {}'.format(puerto))
nodo.register_function(nodo.recibir_informacion, 'enviar_informacion')
nodo.serve_forever()
