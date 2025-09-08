import paho.mqtt.client as mqtt
import json


class OverlordControlZigbee:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__broker = "192.168.0.11"
        self.__light_set = "zigbee2mqtt/Light/set"
        self.__charger_set = "zigbee2mqtt/Charger/set"
        self.__client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

    def overlord_control_zigbee_start(self, **kwargs):
        print("Overlord Control Zigbee готов к работе")

    def light(self, state=None, **kwargs):
        self.__client.connect(self.__broker, 1883, 60)
        string = '{"state": "' + str(state) + '"}'
        self.__client.publish(self.__light_set, string)
        self.__client.disconnect()
        return self.__light_set, "<<<", string

    def charger(self, state=None, **kwargs):
        self.__client.connect(self.__broker, 1883, 60)
        string = '{"state": "' + str(state) + '"}'
        self.__client.publish(self.__charger_set, string)
        self.__client.disconnect()
        return self.__charger_set, "<<<", '{"state": "ON"}'
