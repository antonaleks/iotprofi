import json
import time
from asyncio import sleep
from random import random
from threading import Thread

from flask import Flask, render_template

from mqtt import MQTTClient

app = Flask(__name__)

sensors = [
    {
        "id": "temperature",
        "name": "Температура",
        "topic": 'base/state/temperature',
        "value": int(random()*100)
    },
    {
        "id": "humidity",
        "name": "Влажность",
        "topic": 'base/state/humidity',
        "value": int(random()*100)
    },
    {
        "id": "distance",
        "name": "Расстояние",
        "topic": 'base/state/distance',
        "value": int(random()*100)
    },
]


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
        for sensor in sensors:
            sensor["value"] = int(random()*100)
        time.sleep(1)


if __name__ == '__main__':
    Thread(target=simulate_data, daemon=True).start()
    client = MQTTClient(sensors=sensors)
    client.start()
    print("ok")
    app.run()
