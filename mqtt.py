from threading import Thread

import time

import paho.mqtt.client as mqtt

mqtt_cred = {
    "hostname": "sandbox.rightech.io",
    "port": 1883,
    "client_id": "mqtt-iprofi_217237338-slg24t",
    "keep_alive": 60
}


class MQTTClient(Thread):

    def __init__(self, host=mqtt_cred['hostname'], port=mqtt_cred['port'], client_id=mqtt_cred['client_id'],
                 keep_alive=mqtt_cred['keep_alive'], sensors=None, sensors_request=None):
        super().__init__()
        self.host = host
        self.port = port
        self.client_id = client_id
        self.keep_alive = keep_alive
        self.sensors = sensors
        self.sensors_request = sensors_request
        self.client = mqtt.Client(client_id="mqtt-iprofi_217237338-slg24t")
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        self.client.connect("sandbox.rightech.io", 1883, 60)

        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        self.client.subscribe("$SYS/#")

    def on_message(self, client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))
        print("i can do action")

    def request_pub(self):
        for sensor in self.sensors_request:
            self.client.publish(sensor["topic"], sensor["value"])

    def run(self) -> None:
        while True:
            for sensor in self.sensors:
                self.client.publish(sensor["topic"], sensor["value"])
                time.sleep(1)


if __name__ == "__main__":
    client = MQTTClient(sensors=[{"topic": 'base/state/temperature', "value": 222}])
    client.start()
    print("ok")
