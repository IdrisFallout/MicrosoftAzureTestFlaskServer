from flask import Flask, request
from flask_socketio import SocketIO, emit, join_room

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello Microsoft Azure Room2!'


if __name__ == '__main__':
    app.run()
