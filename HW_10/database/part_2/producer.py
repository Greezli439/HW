from model_mongodb import Consumer
from db_connection import connect
import json
import pika
import faker

fake = faker.Faker()

credentials = pika.PlainCredentials('guest', 'guest')
conn_sting = pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials)
connection = pika.BlockingConnection(conn_sting)

channel = connection.channel()
channel.queue_declare(queue='message')

def create_new_records():
    message = {}
    name, email = fake.name(), fake.email()
    data = Consumer(name=name, email=email, notified=False)
    data.save()
    message['name'] = name
    message['email'] = email
    message['id'] = str(data.id)
    print(message)
    return message
def send_message_data_to_email_provider():
    message = create_new_records()

    channel.basic_publish(exchange='', routing_key='message', body=json.dumps(message).encode())



if __name__ == '__main__':
    for i in range(100):
        send_message_data_to_email_provider()
    connection.close()



