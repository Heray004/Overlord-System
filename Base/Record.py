from datetime import datetime
import json
import pyaudio
from vosk import Model, KaldiRecognizer
from time import sleep, time

class Record:
    def __init__(self, devices):
        self.model = Model(r"vosk-model-small-ru-0.22")
        self.p = pyaudio.PyAudio()
        self.devices = devices
        self.microphone_search()

    def microphone_search(self):
        self.numdevices = self.p.get_host_api_info_by_index(0).get('deviceCount')
        for device in self.devices:
            for i in range(0, self.numdevices):
                if (self.p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                    if device in self.p.get_device_info_by_host_api_device_index(0, i).get('name'):
                        self.devices[device][0] = i
                        self.devices[device][1] = KaldiRecognizer(self.model, 16000)
                        try:
                            self.devices[device][2] = self.p.open(
                                format=pyaudio.paInt16,
                                channels=1, rate=16000,
                                input=True,
                                frames_per_buffer=4000,
                                input_device_index=self.devices[device][0]
                            )
                            self.devices[device][2].start_stream()
                            print(f"Микрофон {device} найден")
                        except:
                            self.devices[device][2] = None
                            print(f"Микрофон {device} не найден")
        s = 0
        for device, param in self.devices.items():
            if (param[0] is not None) and (param[2] is not None):
                s += 1
            else:
                del self.devices[device]
        print(f"Количество записывающих устройств - {s}")
        self.example = []
        for device in self.devices.items():
            self.example.append(None)
        return self.devices

    def listen(self):
        while True:
            self.text = list(self.example)
            i = 0
            for device, param in self.devices.items():
                self.data = param[2].read(4000, exception_on_overflow=False)
                if param[1].AcceptWaveform(self.data) and len(self.data) > 0:
                    self.answer = json.loads(param[1].Result())
                    if self.answer["text"]:
                        self.text[i] = self.answer["text"]
                i += 1
            if self.text != self.example:
                if None in self.text:
                    i = 0
                    for device, param in self.devices.items():
                        if self.text[i] == None:
                            self.data = param[2].read(4000, exception_on_overflow=False)
                            if param[1].AcceptWaveform(self.data) and len(self.data) > 0:
                                self.answer = json.loads(param[1].Result())
                                if self.answer["text"]:
                                    self.text[i] = self.answer["text"]
                        i += 1
                dat = datetime.now()
                print(f" {dat.day}.{dat.month}.{dat.year}-{dat.hour}:{dat.minute}:{dat.second}", end=" ")
                yield self.text

    def listen_one_msg(self):
        while True:
            self.text = list(self.example)
            i = 0
            for device, param in self.devices.items():
                self.data = param[2].read(4000, exception_on_overflow=False)
                if param[1].AcceptWaveform(self.data) and len(self.data) > 0:
                    answer = json.loads(param[1].Result())
                    if answer["text"]:
                        self.text[i] = answer["text"]
                i += 1
            if self.text != self.example:
                if None in self.text:
                    i = 0
                    for device, param in self.devices.items():
                        if self.text[i] == None:
                            self.data = param[2].read(4000, exception_on_overflow=False)
                            if param[1].AcceptWaveform(self.data) and len(self.data) > 0:
                                answer = json.loads(param[1].Result())
                                if answer["text"]:
                                    self.text[i] = answer["text"]
                        i += 1
                dat = datetime.now()
                print(f" {dat.day}.{dat.month}.{dat.year}-{dat.hour}:{dat.minute}:{dat.second}", end=" ")
                return self.text
