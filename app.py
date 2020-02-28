import json
import time
from asyncio import sleep
from random import random
from threading import Thread

from flask import Flask, render_template

app = Flask(__name__)

sensors = {"sensor1": random(), "sensor2": random(), "sensor3": random(), "sensor4": random()}


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/read-sensor-value')
def read_sensor_value():
    return json.dumps({'data': sensors}, ensure_ascii=False)


@app.route('/read-sensor-request')
def read_sensor_request():
    return json.dumps({'data': sensors}, ensure_ascii=False)


def simulate_data():
    global sensors
    i=0
    while True:
        i=i+1
        sensors = {"sensor1": random(), "sensor2": random(), "sensor3": random(), "sensor4": i}
        time.sleep(1)


if __name__ == '__main__':
    Thread(target=simulate_data, daemon=True).start()
    app.run()
