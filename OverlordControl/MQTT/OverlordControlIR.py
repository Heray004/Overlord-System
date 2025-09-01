import paho.mqtt.client as mqtt
import json


class OverlordControlIR:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.broker_ir = "192.168.0.11"
        self.media_topic = "Overlord_Control/volume/set"
        self.conditioner_mode_topic = "Overlord_Control/conditioner/mode/set"
        self.conditioner_fan_mode_topic = "Overlord_Control/conditioner/fan_mode/set"
        self.conditioner_temperature_topic = "Overlord_Control/conditioner/temperature/set"

    def overlord_control_ir_start(self, **kwargs):
        self.client_ir = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        print("Overlord Control IR готов к работе")

    def conditioner_mod(self, mod=None, **kwargs):
        self.client_ir.connect(self.broker_ir, 1883, 60)
        self.client_ir.publish(self.conditioner_mode_topic, mod)
        self.client_ir.disconnect()
        return self.conditioner_mode_topic, "<<<", mod

    def vol_set(self, vol=None, **kwargs):
        self.client_ir.connect(self.broker_ir, 1883, 60)
        self.client_ir.publish(self.media_topic, vol)
        self.client_ir.disconnect()
        return self.media_topic, "<<<", vol

