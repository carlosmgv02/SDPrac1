import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('162.246.254.134'))

channel = connection.channel()
channel.queue_declare(queue='client-server')
connection.close()

