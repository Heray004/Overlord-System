import pickle
import numpy as np
from collections import Counter
from threading import Thread
from time import sleep
# -------------------------------------------
from Base.WordBase import WordBase
from Base.BaseFunction import BaseFunction
from OverlordControl.Arduino.OverlordControlIR import OverlordControlIR
from OverlordControl.Zigbee.OverlordControlZigbee import OverlordControlZigbee
from OverlordAccess.HomeAssistant.OverlordAccessHA import OverlordAccessHA
# -------------------------------------------


class Recognition(WordBase, BaseFunction, OverlordControlIR, OverlordControlZigbee, OverlordAccessHA):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with open(r"DecisionModel/Overlord_model_v0.1.pkl", "rb") as model_file:
            self.model_pipeline = pickle.load(model_file)
        self.name_flag = False
        self.name_score = 0

    def Recognition_start(self, model_flag):
        self.OverlordControl_IR_start()
        self.OverlordControl_Zigbee_start()
        ha = Thread(target=self.OverlordAccess_HA_start, args=(model_flag, self,), daemon=True)
        ha.start()
        sleep(0.1)

    def merge_text(self, text):
        text = list(filter(None.__ne__, text))
        if len(text) == 1:
            return text[0]
        tokenized_messages = [msg.split() for msg in text]
        word_counts = Counter(word for msg in tokenized_messages for word in msg)
        reference_message = max(text, key=len)
        reference_words = reference_message.split()
        merged_text = []
        used_words = set()
        for ref_word in reference_words:
            if word_counts[ref_word] > 1:  # Слово должно встречаться хотя бы в двух сообщениях
                merged_text.append(ref_word)
                used_words.add(ref_word)
        for message in tokenized_messages:
            for word in message:
                if word not in used_words and word_counts[word] > 1:
                    merged_text.append(word)
                    used_words.add(word)

        merged_text = " ".join(merged_text)
        return merged_text

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
                intent = "BaseFunction.another"
            else:
                intent = self.model_pipeline.predict([text])[0]  # Предсказание метки
                probs = self.model_pipeline.predict_proba([text])[0]
                max_prob = np.max(probs)
                if max_prob < 0.6:
                    intent = "BaseFunction.another"
            intent = intent.split('.')
            if intent[1] != "another":
                print(intent)
                try:
                    s = getattr(self, intent[1])()
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

