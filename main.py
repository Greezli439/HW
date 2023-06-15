from flask import Flask, render_template, request
from threading import Thread
import datetime
import json
import socket
from time import sleep
from pathlib import Path

'''
docker build /Users/mykhailo/studies/go_it/2.0/HW -t hw_4

docker run -d -p 3000:5000 -v /Users/mykhailo/studies/go_it/2.0/HW/storage:/app/storage hw_4

docker ps
docker inspect 

http://0.0.0.0:3000/m
'''

def run_server():
    app = Flask(__name__)
    my_socket_sender = socket.socket()
    my_socket_sender.connect(('localhost', 3000))

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('error.html')

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/message', methods=['POST', 'GET'])
    def message():
        if request.method == 'POST':
            username = request.form.get('username')
            message = request.form.get('message')

            #тут новий клієнт для збереження в файл
            #сделать подключение один раз


            data = json.dumps((username, message))
            my_socket_sender.sendall(data.encode('utf-8'))


        return render_template('message.html')

    app.run(debug=False, host='0.0.0.0')

def start_socket_client():
    my_socket_client = socket.socket()
    my_socket_client.bind(('localhost', 3000))
    my_socket_client.listen(1)
    connection, adress = my_socket_client.accept()
    while True:
        data = connection.recv(1024)
        data = data.decode('utf-8')
        data = json.loads(data)

        with open('storage/data.json', 'r') as f:
            data_from_file = json.load(f)
        data_from_file[str(datetime.datetime.now())] = {'username': data[0], 'message': data[1]}

        with open('storage/data.json', 'w') as f:
            json.dump(data_from_file, f)

def check_data_file():
    if not Path('storage/data.json').is_file():
        create_data_file()

def create_data_file():
    Path('storage').mkdir()
    Path('storage/data.json').touch()
    with open('storage/data.json', 'w') as f:
        json.dump({}, f)

if __name__ == '__main__':

    check_data_file()
    thread_for_socket_client = Thread(target=start_socket_client)
    thread_for_socket_client.start()
    sleep(1)
    thread_for_server = Thread(target=run_server)
    thread_for_server.start()
