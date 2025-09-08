import pickle
import numpy as np
from threading import Thread
from time import sleep
# -------------------------------------------
from Base.BaseFunction import BaseFunction
from Base.DatabaseRead import DatabaseRead
from OverlordControl.MQTT.OverlordControlIR import OverlordControlIR
from OverlordControl.MQTT.OverlordControlZigbee import OverlordControlZigbee
# from OverlordAccess.HomeAssistant.OverlordAccessHA import OverlordAccessHA
# -------------------------------------------


class Recognition(BaseFunction, DatabaseRead, OverlordControlIR, OverlordControlZigbee):  # OverlordAccessHA
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with open(r"DecisionModel/Overlord_model_v0.1.pkl", "rb") as model_file:
            self.model_pipeline = pickle.load(model_file)
        self.name_flag = False
        self.name_score = 0

    def recognition_start(self):
        self.overlord_control_ir_start()
        self.overlord_control_zigbee_start()
        # ha = Thread(target=self.overlord_access_ha_start, daemon=True)
        # ha.start()
        sleep(0.1)

    def model_recognition(self, text):
        words = text.split()
        if len(words) > 3:
            intent = ["another", "None"]
        else:
            intent = self.model_pipeline.predict([text])[0]  # Предсказание метки
            probs = self.model_pipeline.predict_proba([text])[0]
            max_prob = np.max(probs)
            if max_prob < 0.6:
                intent[0] = "another"
        if intent[0] != "another":
            print(intent[0], intent[1])
            try:
                s = getattr(self, intent[0])(**eval(intent[1]))
                print(s, "\n\n")
            except AttributeError as E:
                print("комманда распознанна, но не имеет функции\n", E)
        else:
            print(intent, "\n\n")
