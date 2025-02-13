import paho.mqtt.client as mqtt
import json


class OverlordControlZigbee:
    def __init__(self):
        self.BROKER = "localhost"
        self.light_set = "zigbee2mqtt/Light/set"
        self.charger_set = "zigbee2mqtt/Charger/set"
        # self.light_get = "zigbee2mqtt/Light/get"
        # self.charger_get = "zigbee2mqtt/Charger/get"
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        # self.client.on_message = self.on_message
        # self.data = 123


    def light_on(self):
        self.client.connect(self.BROKER, 1883, 60)
        self.client.publish(self.light_set, '{"state": "ON"}')
        self.client.disconnect()

    def light_off(self):
        self.client.connect(self.BROKER, 1883, 60)
        self.client.publish(self.light_set, '{"state": "OFF"}')
        self.client.disconnect()

    # def light(self):
    #     self.client.connect(self.BROKER, 1883, 60)
    #     if self.light_flag is True:
    #         self.client.publish(self.light_set, '{"state": "OFF"}')
    #         self.light_flag = False
    #     elif self.light_flag is False:
    #         self.client.publish(self.light_set, '{"state": "ON"}')
    #         self.light_flag = True
    #     self.client.disconnect()

    def charger_on(self):
        self.client.connect(self.BROKER, 1883, 60)
        self.client.publish(self.charger_set, '{"state": "ON"}')
        self.client.disconnect()

    def charger_off(self):
        self.client.connect(self.BROKER, 1883, 60)
        self.client.publish(self.charger_set, '{"state": "OFF"}')
        self.client.disconnect()

    # def charger(self):
    #     self.client.connect(self.BROKER, 1883, 60)
    #     if self.charger_flag is True:
    #         self.client.publish(self.charger_set, '{"state": "OFF"}')
    #         self.charger_flag = False
    #     elif self.charger_flag is False:
    #         self.client.publish(self.charger_set, '{"state": "ON"}')
    #         self.charger_flag = True
    #     self.client.disconnect()
