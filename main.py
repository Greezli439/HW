from flask import Flask, render_template, request
from threading import Thread
import datetime
import json

def run_server():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/message', methods=['POST', 'GET'])
    def message():
        if request.method == 'POST':
            username = request.form.get('username')
            message = request.form.get('message')

            #тут новий клієнт для збереження в файл
            with open('storage/data.json', 'r') as f:
                data_from_file = json.load(f)
            data_from_file[str(datetime.datetime.now())] = {'username': username, 'message': message}

            with open('storage/data.json', 'w') as f:
                json.dump(data_from_file, f)

            print(message, username)

        return render_template('message.html')

    app.run()


if __name__ == '__main__':
    thread_for_server = Thread(target=run_server)
    thread_for_server.start()
