import paho.mqtt.client as mqtt
import json


class OverlordAccessHA:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.broker_ha2pc = "192.168.0.11"
        self.client_ha2pc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.client_ha2pc.on_connect = self.on_connect
        self.client_ha2pc.on_message = self.on_message
        with open(r"OverlordAccess/HomeAssistant/config.json", 'r') as config_json:
            self.config_dict = json.loads(config_json.read())
        self.client_ha2pc.connect(self.broker_ha2pc, 1883, 60)

    def overlord_access_ha_start(self):
        print("Overlord Access HA готов к работе")
        self.client_ha2pc.loop_forever()

    def on_connect(self, client, userdata, flags, rc, properties=None):
        for name, setings in self.config_dict.items():
            self.client_ha2pc.publish(setings["topic"]["HA_conf"], json.dumps(setings["config"]), retain=True)
            for topic in setings["topic"]["availability_topic"]:
                self.client_ha2pc.publish(topic, "online", retain=True)
            for topic in setings["topic"]["command_topic"]:
                self.client_ha2pc.subscribe(topic)
        self.client_ha2pc.subscribe("Overlord_Control/media/set")

    def on_message(self, client, userdata, msg):
        msg_load = str(msg.payload.decode("utf-8"))
        print(f"{msg.topic} >>> {msg_load}")
        try:
            s = getattr(self, msg_load)()
            name = msg.topic.split("/")[2]
            if name in self.config_dict:
                if (s is not None) and (self.config_dict[name]["topic"]["state_topic"][0] != "None"):
                    if len(self.config_dict[name]["topic"]["state_topic"]) == 1:
                        self.client_ha2pc.publish(self.config_dict[name]["topic"]["state_topic"][0], str(s), retain=False)
            print(s, "\n\n")
        except AttributeError as E:
            print("комманда распознанна, но не имеет функции\n", E)
