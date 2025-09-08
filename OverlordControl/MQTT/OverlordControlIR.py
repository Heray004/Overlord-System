import paho.mqtt.client as mqtt
import json


class OverlordControlIR:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__broker = "192.168.0.11"
        self.__media_topic = "Overlord_Control/volume/set"
        self.__conditioner_mode_topic = "Overlord_Control/conditioner/mode/set"
        self.__conditioner_fan_mode_topic = "Overlord_Control/conditioner/fan_mode/set"
        self.__conditioner_temperature_topic = "Overlord_Control/conditioner/temperature/set"
        self.__client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

    def overlord_control_ir_start(self, **kwargs):
        print("Overlord Control IR готов к работе")

    def conditioner_mod(self, mod=None, **kwargs):
        self.__client.connect(self.__broker, 1883, 60)
        self.__client.publish(self.__conditioner_mode_topic, mod)
        self.__client.disconnect()
        return self.__conditioner_mode_topic, "<<<", mod

    def vol_set(self, vol=None, **kwargs):
        self.__client.connect(self.__broker, 1883, 60)
        self.__client.publish(self.__media_topic, vol)
        self.__client.disconnect()
        return self.__media_topic, "<<<", vol
