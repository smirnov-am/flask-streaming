import os
from flask import Flask
from flask_socketio import SocketIO
from plotting import plotting_blueprint
from streaming import bootstrap_on_connect


def create_app(register_blueprint=True):
    app = Flask(__name__)
    app.secret_key = os.urandom(42)
    if register_blueprint:
        app.register_blueprint(plotting_blueprint)

    socketio = SocketIO(app, message_queue='redis://localhost:6379/')
    socketio.on_event('connect', bootstrap_on_connect)
    return socketio, app


socketio, application = create_app()


if __name__ == '__main__':
    socketio.run(application)
