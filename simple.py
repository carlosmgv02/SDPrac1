import pika


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


connection = pika.BlockingConnection(pika.ConnectionParameters('162.246.254.134'))

channel = connection.channel()
channel.queue_declare(queue='client-server')
channel.queue_declare(queue='proxy-terminal')
channel.basic_publish(exchange='',
                      routing_key='client-server',
                      body='Hello World!')
# channel.basic_consume(queue='hello',
#                       auto_ack=True,
#                       on_message_callback=callback)
connection.close()
