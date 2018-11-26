import time
from datetime import datetime
from psutil import cpu_percent
from flask_socketio import emit, SocketIO

DATE_FMT = "%Y-%m-%d %H:%M:%S"


def bootstrap_on_connect():
    emit('bootstrap', {'x': [datetime.now().strftime(DATE_FMT)], 'y': [0]})


def update_plot():
    socketio = SocketIO(message_queue='redis://localhost:6379/')
    while True:
        datetime_now = datetime.now().strftime(DATE_FMT)
        cpu_percent_second = cpu_percent(interval=1)
        socketio.emit('update', {'x': [datetime_now], 'y': [cpu_percent_second]})
        time.sleep(1)


if __name__ == '__main__':
    update_plot()
