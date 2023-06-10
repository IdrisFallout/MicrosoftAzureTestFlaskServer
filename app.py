from flask import Flask, request
from flask_socketio import SocketIO, emit, join_room

app = Flask(__name__)
app.secret_key = 'random secret key!'
socketio = SocketIO(app, cors_allowed_origins="*")


# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello Microsoft Azure update 4!'


if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=5000)
