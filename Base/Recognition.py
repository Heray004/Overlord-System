import pickle
import numpy as np
from threading import Thread
from time import sleep
# -------------------------------------------
from Base.WordBase import WordBase
from Base.BaseFunction import BaseFunction
from OverlordControl.MQTT.OverlordControlIR import OverlordControlIR
from OverlordControl.MQTT.OverlordControlZigbee import OverlordControlZigbee
from OverlordAccess.HomeAssistant.OverlordAccessHA import OverlordAccessHA
# -------------------------------------------


class Recognition(WordBase, BaseFunction, OverlordControlIR, OverlordControlZigbee, OverlordAccessHA):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with open(r"DecisionModel/Overlord_model_v0.1.pkl", "rb") as model_file:
            self.model_pipeline = pickle.load(model_file)
        self.name_flag = False
        self.name_score = 0

    def recognition_start(self, model_flag):
        self.overlord_control_ir_start()
        self.overlord_control_zigbee_start()
        ha = Thread(target=self.overlord_access_ha_start, daemon=True)
        ha.start()
        sleep(0.1)

    def list_recognition(self, text):
        # --------------------------------------------------------------------------------------------------------------
        for k, v in self.word_base['other'].items():
            if text in v:
                try:
                    getattr(self, k[1])()
                except AttributeError:
                    print("комманда распознанна, но не имеет функции")

        # --------------------------------------------------------------------------------------------------------------
        for name in self.word_base["name"]:
            if name in text:
                self.name_flag = True
                self.name_score = 0
                if text.startswith(name):
                    text = text.replace(name + " ", "")
                elif text.endswith(name):
                    text = text.replace(" " + name, "")
                else:
                    text = text.replace(" " + name + " ", " ")

        # --------------------------------------------------------------------------------------------------------------
        if self.name_flag:
            self.name_score += 1
            for k, v in self.word_base['commands'].items():
                if text in v:
                    self.name_flag = False
                    self.name_score = 0
                    try:
                        getattr(self, k[1])()
                    except AttributeError:
                        print("комманда распознанна, но не имеет функции")

        if self.name_score == 3:
            self.name_score = 0
            self.name_flag = False

        # --------------------------------------------------------------------------------------------------------------
    def model_recognition(self, text):
        # if type(text) is str:
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
        # elif type(text) is list:
        #     intent = ["BaseFunction.another"]*len(text)
        #     for i in range(len(text)):
        #         if text[i] is not None:
        #             self.words = text[i].split()
        #             if len(self.words) > 3:
        #                 intent[i] = "BaseFunction.another"
        #             else:
        #                 intent[i] = self.model_pipeline.predict([text[i]])[0]  # Предсказание метки
        #                 probs = self.model_pipeline.predict_proba([text[i]])[0]
        #                 max_prob = np.max(probs)
        #                 if max_prob < 0.6:
        #                     intent[i] = "BaseFunction.another"
        #             print(intent, "\n\n")
        #     intent = self.merge_text(intent)
        #     intent = intent.split('.')
        #     if intent[1] != "another":
        #         try:
        #             getattr(eval(intent[0]), intent[1])()
        #         except AttributeError:
        #             print("комманда распознанна, но не имеет функции")

