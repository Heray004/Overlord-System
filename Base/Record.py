from datetime import datetime
import json
import pyaudio
from vosk import Model, KaldiRecognizer
from time import sleep, time

class Record:
    def __init__(self):
        self.model = Model(r"vosk-model-small-ru-0.22")
        self.p = pyaudio.PyAudio()

    def microphone_search(self):
        devices = {
            "fifine": [None, None, None],
            "Petlya": [None, None, None]
        }
        numdevices = self.p.get_host_api_info_by_index(0).get('deviceCount')
        for device in devices:
            for i in range(0, numdevices):
                if (self.p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                    if device in self.p.get_device_info_by_host_api_device_index(0, i).get('name'):
                        devices[device][0] = i
                        devices[device][2] = KaldiRecognizer(self.model, 16000)
                        try:
                            devices[device][1] = self.p.open(
                                format=pyaudio.paInt16,
                                channels=1, rate=16000,
                                input=True,
                                frames_per_buffer=8000,
                                input_device_index=devices[device][0]
                            )
                            devices[device][1].start_stream()
                            print(f"Микрофон {device} найден")
                        except:
                            devices[device][1] = None
                            print(f"Микрофон {device} не найден")
        s = 0
        for device, param in devices.items():
            if (param[0] is not None) and (param[1] is not None):
                s += 1
            else:
                del devices[device]
        print(f"Количество записывающих устройств - {s}")
        return devices

    def listen(self, devices):
        example = []
        for device in devices.items():
            example.append(None)
        while True:
            text = []
            for device in devices.items():
                text.append(None)
            i = 0
            for device, param in devices.items():
                data = param[1].read(8000, exception_on_overflow=False)
                if param[2].AcceptWaveform(data) and len(data) > 0:
                    answer = json.loads(param[2].Result())
                    if answer["text"]:
                        text[i] = answer["text"]
                i+=1
            if text != example:
                if None in text:
                    i = 0
                    for device, param in devices.items():
                        if text[i] == None:
                            data = param[1].read(8000, exception_on_overflow=False)
                            if param[2].AcceptWaveform(data) and len(data) > 0:
                                answer = json.loads(param[2].Result())
                                if answer["text"]:
                                    text[i] = answer["text"]
                        i += 1
                dat = datetime.now()
                print(f" {dat.day}.{dat.month}.{dat.year}-{dat.hour}:{dat.minute}:{dat.second}", end=" ")
                yield text

    def listen_one_msg(self, devices):
        example = []
        for device in devices.items():
            example.append(None)
        while True:
            text = []
            for device in devices.items():
                text.append(None)
            i = 0
            for device, param in devices.items():
                data = param[1].read(8000, exception_on_overflow=False)
                if param[2].AcceptWaveform(data) and len(data) > 0:
                    answer = json.loads(param[2].Result())
                    if answer["text"]:
                        text[i] = answer["text"]
                i += 1
            if text != example:
                if None in text:
                    i = 0
                    for device, param in devices.items():
                        if text[i] == None:
                            data = param[1].read(8000, exception_on_overflow=False)
                            if param[2].AcceptWaveform(data) and len(data) > 0:
                                answer = json.loads(param[2].Result())
                                if answer["text"]:
                                    text[i] = answer["text"]
                        i += 1
                dat = datetime.now()
                print(f" {dat.day}.{dat.month}.{dat.year}-{dat.hour}:{dat.minute}:{dat.second}", end=" ")
                return text
