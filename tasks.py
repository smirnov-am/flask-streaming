import time
from datetime import timedelta, date
from flask_socketio import SocketIO


def update_plot():
    x = (date(2018, 1, 1)+timedelta(days=299))
    socketio = SocketIO(message_queue='redis://localhost:6379/')
    while True:
        x = x + timedelta(days=1)
        socketio.send({'x': x.strftime("%Y-%m-%d"), 'y': 1})
        time.sleep(1)


update_plot()