import paho.mqtt.client as mqtt
import json


class OverlordControlZigbee:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__broker_z2m = "192.168.0.11"
        self.__light_set = "zigbee2mqtt/Light/set"
        self.__charger_set = "zigbee2mqtt/Charger/set"
        self.__client_z2m = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

    def overlord_control_zigbee_start(self, **kwargs):
        print("Overlord Control Zigbee готов к работе")

    def light(self, state=None, **kwargs):
        self.__client_z2m.connect(self.__broker_z2m, 1883, 60)
        string = '{"state": "' + str(state) + '"}'
        self.__client_z2m.publish(self.__light_set, string)
        self.__client_z2m.disconnect()
        return self.__light_set, "<<<", string

    def charger(self, state=None, **kwargs):
        self.__client_z2m.connect(self.__broker_z2m, 1883, 60)
        string = '{"state": "' + str(state) + '"}'
        self.__client_z2m.publish(self.__charger_set, string)
        self.__client_z2m.disconnect()
        return self.__charger_set, "<<<", '{"state": "ON"}'
