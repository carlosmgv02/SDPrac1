import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('162.246.254.134'))

channel = connection.channel()
channel.queue_declare(queue='client-server')
channel.basic_publish(exchange='',
                      routing_key='client-server',
                        body='Hello World!')
connection.close()

