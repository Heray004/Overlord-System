import paho.mqtt.client as mqtt
import json


class OverlordControl_Zigbee:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.broker_z2m = "192.168.0.11"
        self.light_set = "zigbee2mqtt/Light/set"
        self.charger_set = "zigbee2mqtt/Charger/set"

    def OverlordControl_Zigbee_start(self):
        self.client_z2m = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        print("Overlord Control Zigbee готов к работе")

    def light_on(self):
        self.client_z2m.connect(self.broker_z2m, 1883, 60)
        self.client_z2m.publish(self.light_set, '{"state": "ON"}')
        self.client_z2m.disconnect()
        return self.light_set, "<<<", '{"state": "ON"}'

    def light_off(self):
        self.client_z2m.connect(self.broker_z2m, 1883, 60)
        self.client_z2m.publish(self.light_set, '{"state": "OFF"}')
        self.client_z2m.disconnect()
        return self.light_set, "<<<", '{"state": "OFF"}'

    def charger_on(self):
        self.client_z2m.connect(self.broker_z2m, 1883, 60)
        self.client_z2m.publish(self.charger_set, '{"state": "ON"}')
        self.client_z2m.disconnect()
        return self.charger_set, "<<<", '{"state": "ON"}'

    def charger_off(self):
        self.client_z2m.connect(self.broker_z2m, 1883, 60)
        self.client_z2m.publish(self.charger_set, '{"state": "OFF"}')
        self.client_z2m.disconnect()
        return self.charger_set, "<<<", '{"state": "OFF"}'
