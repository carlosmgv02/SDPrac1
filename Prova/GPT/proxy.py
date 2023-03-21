import xmlrpc.client
import time

# Leer el archivo de configuración
with open('terminales.cfg', 'r') as f:
    # Crear una lista de terminales
    terminales = [line.strip() for line in f]

# Crear el proxy con la lista de terminales
proxies = [xmlrpc.client.ServerProxy(terminal) for terminal in terminales]

# Distribuir la información utilizando una planificación round robin
n_terminales = len(terminales)
i = 0
while True:
    # Obtener el índice de la siguiente terminal en la lista
    indice_terminal = i % n_terminales

    # Obtener el proxy de la siguiente terminal
    proxy = proxies[indice_terminal]

    # Enviar la información a la terminal
    proxy.enviar_informacion('informacion')

    # Esperar un tiempo antes de la siguiente iteración
    time.sleep(1)

    # Incrementar el índice para la siguiente iteración
    i += 1
