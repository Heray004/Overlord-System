import paho.mqtt.client as mqtt
import json


class OverlordAccess_HA:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.broker_ha2pc = "192.168.0.11"
        self.client_ha2pc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.client_ha2pc.on_connect = self.on_connect
        self.client_ha2pc.on_message = self.on_message

    def OverlordAccess_HA_start(self, type_recognition, Recognition):
        self.type_recognition = type_recognition
        self.Recognition = Recognition
        self.client_ha2pc.connect(self.broker_ha2pc, 1883, 60)
        print("Overlord Control HA готов к работе")
        self.client_ha2pc.loop_forever()

    def on_connect(self, client, userdata, flags, rc, properties=None):
        self.client_ha2pc.subscribe("ha2pc")

    def on_message(self, client, userdata, msg):
        self.msg = json.loads(msg.payload.decode("utf-8"))
        print(f"{msg.topic} >>> {self.msg['text']}")
        if self.type_recognition == 0:
            self.Recognition.list_recognition(self.msg["text"])
        elif self.type_recognition == 1:
            self.Recognition.model_recognition(self.msg["text"])

