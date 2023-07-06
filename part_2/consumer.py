import json

import pika
from time import sleep

from model_mongodb import Consumer
from db_connection import connect


credentials = pika.PlainCredentials('guest', 'guest')
conn_sting = pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials)
connection = pika.BlockingConnection(conn_sting)

channel = connection.channel()
channel.queue_declare(queue='message')

def change_flag(id):
    note = Consumer.objects(id=id)
    note.update(notified=True)


def simulation_sending_email(data):
    sleep(1)
    # email was successful sent
    return True
def callback(ch, method, properties, body):
    data = json.loads(body)
    print(data)
    result = simulation_sending_email(data)
    if result:
        change_flag(data['id'])
    ch.basic_ack(delivery_tag=method.delivery_tag)




channel.basic_consume(queue='message', on_message_callback=callback)
channel.basic_qos(prefetch_count=1)


channel.start_consuming()


