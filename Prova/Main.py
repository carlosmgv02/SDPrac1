import threading
from Node import Node

# Crear los nodos/servidores
node1 = Node('Node 1', 'localhost', 8001)
node2 = Node('Node 2', 'localhost', 8002)
node3 = Node('Node 3', 'localhost', 8003)

# Añadir los nodos/servidores como peers
node1.add_peer(node2)
node1.add_peer(node3)
node2.add_peer(node1)
node2.add_peer(node3)
node3.add_peer(node1)
node3.add_peer(node2)
# Iniciar el sistema distribuido
node1.add('key1', 'value1')
node1.add('key2', 'value2')
node2.add('key3', 'value3')

# Comprobar que los valores se han añadido correctamente
print('Valor de key1 en Node 1:', node1.get('key1'))
print('Valor de key2 en Node 2:', node2.get('key2'))
print('Valor de key3 en Node 3:', node3.get('key3'))

# Eliminar un valor
node3.delete('key1')

# Comprobar que el valor se ha eliminado correctamente
print('Valor de key1 en Node 1:', node1.get('key1'))

