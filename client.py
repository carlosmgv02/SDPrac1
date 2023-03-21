import xmlrpc.client
from Persona import Persona
from Dirección import Direccion
import jsonpickle
import base64

direccion = Direccion("Calle 123", 2)
persona = Persona("Juan", 30, direccion, "555-1234", "juan@example.com")

persona_bytes = jsonpickle.encode(persona).encode('utf-8')
persona_base64 = base64.b64encode(persona_bytes).decode('utf-8')
proxy = xmlrpc.client.ServerProxy('http://localhost:4000/')
proxy.add_user('pruebaObjeto',persona_base64)
print('EL PROGRAMA FUNCIONA: ')
print(proxy.get_user('pruebaObjeto'))
prueba = base64.b64decode(proxy.get_user('pruebaObjeto')).decode('utf-8')
print(jsonpickle.decode(prueba))

proxy.subscribe('cola')
