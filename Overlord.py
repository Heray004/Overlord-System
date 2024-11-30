import json
import pyaudio
from vosk import Model, KaldiRecognizer
# from threading import Thread
from datetime import datetime

def module_search():
    # Thread(target=listen_port, daemon=True).start()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    for i in range(0, numdevices):
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            if "fifine" in p.get_device_info_by_host_api_device_index(0, i).get('name'):
                micro1_name = p.get_device_info_by_host_api_device_index(0, i).get('name')
                micro1_index = i
            if "Petlya" in p.get_device_info_by_host_api_device_index(0, i).get('name'):
                micro2_name = p.get_device_info_by_host_api_device_index(0, i).get('name')
                micro2_index = i
    try:
        stream1 = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True,
                         frames_per_buffer=8000, input_device_index=micro1_index)
        stream1.start_stream()
        mic1 = True
        print("Микрофон fifine найден")
    except:
        micro1_name = None
        mic1 = False
        stream1 = None
        print("Микрофон fifine не найден")

    try:
        stream2 = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True,
                         frames_per_buffer=8000, input_device_index=micro2_index)
        stream2.start_stream()
        mic2 = True
        print("Микрофон Petlya найден")
    except:
        mic2 = False
        stream2 = None
        micro2_name = None
        print("Микрофон fifine не найден")

    return stream1, stream2, micro1_name, micro2_name, mic1, mic2


def listen_def(stream1, stream2, micro1_name, micro2_name, mic1, mic2):
    if mic1 and mic2:
        print("Количество записывающих устройств - 2")
        rec1 = KaldiRecognizer(model, 16000)
        rec2 = KaldiRecognizer(model, 16000)
        return listen_all(stream1, stream2, rec1, rec2, micro1_name, micro2_name)
    elif mic1:
        print("Количество записывающих устройств - 1")
        rec1 = KaldiRecognizer(model, 16000)
        return listen1(stream1, rec1, micro1_name)
    elif mic2:
        print("Количество записывающих устройств - 1")
        rec2 = KaldiRecognizer(model, 16000)
        return listen2(stream2, rec2, micro2_name)
    elif (not mic1) and (not mic2):
        EXIT("Количество записывающих устройств - 0")


def listen_all(stream1, stream2, rec1, rec2, micro1_name, micro2_name):
    print('Система "Overlord" готова к работе')
    while True:
        data1 = stream1.read(4000, exception_on_overflow=False)
        data2 = stream2.read(4000, exception_on_overflow=False)
        if (rec1.AcceptWaveform(data1) and len(data1) > 0) or (rec2.AcceptWaveform(data2) and len(data2) > 0):
            answer1 = json.loads(rec1.Result())
            answer2 = json.loads(rec2.Result())
            dat = datetime.now()
            if (answer1["text"] and answer2["text"]) and (answer1["text"] == answer2["text"]):
                print(f" {dat.day}.{dat.month}.{dat.year}-{dat.hour}:{dat.minute}:{dat.second} ({micro1_name} + {micro2_name})", end=" ")
                yield answer1["text"]
            else:
                if answer1["text"]:
                    print(f" {dat.day}.{dat.month}.{dat.year}-{dat.hour}:{dat.minute}:{dat.second} ({micro1_name})", end=" ")
                    yield answer1["text"]
                if answer2["text"]:
                    print(f" {dat.day}.{dat.month}.{dat.year}-{dat.hour}:{dat.minute}:{dat.second} ({micro2_name})", end=" ")
                    yield answer2["text"]


def listen1(stream1, rec1, micro1_name):
    print('Система "Overlord" готова к работе')
    while True:
        data1 = stream1.read(4000, exception_on_overflow=False)
        if rec1.AcceptWaveform(data1) and len(data1) > 0:
            answer1 = json.loads(rec1.Result())
            dat = datetime.now()
            if answer1["text"]:
                print(f" {dat.day}.{dat.month}.{dat.year}-{dat.hour}:{dat.minute}:{dat.second} ({micro1_name})", end=" ")
                yield answer1["text"]


def listen2(stream2, rec2, micro2_name):
    print('Система "Overlord" готова к работе')
    while True:
        data2 = stream2.read(4000, exception_on_overflow=False)
        if rec2.AcceptWaveform(data2) and len(data2) > 0:
            answer2 = json.loads(rec2.Result())
            dat = datetime.now()
            if answer2["text"]:
                print(f" {dat.day}.{dat.month}.{dat.year}-{dat.hour}:{dat.minute}:{dat.second} ({micro2_name})", end=" ")
                yield answer2["text"]


if __name__ == "__main__":
    # -------------------------------------------
    model = Model(r"vosk-model-small-ru-0.22")
    p = pyaudio.PyAudio()
    name_flag = False
    name_score = 0
    # -------------------------------------------
    from WordBase import word_base
    from BaseFunction import *
    from Arduino.OverlordControl import *
    # from Arduino.ArduinoGlove import listen_port
    # -------------------------------------------
    OverlordControl = OverlordControl()
    BaseFunction = BaseFunction()

    while True:
        try:
            for text in listen_def(*module_search()):
                print(f'>>> {text}')

# --------------------------------------------------------------------------------------------------------------
                for k, v in word_base['other'].items():
                    if text in v:
                        try:
                            getattr(eval(k[0]), k[1])()
                        except AttributeError:
                            print("комманда распознанна, но не имеет функции")

# --------------------------------------------------------------------------------------------------------------
                for name in word_base["name"]:
                    if name in text:
                        name_flag = True
                        name_score = 0
                        if text.startswith(name):
                            text = text.replace(name + " ", "")
                        elif text.endswith(name):
                            text = text.replace(" " + name, "")
                        else:
                            text = text.replace(" " + name + " ", " ")

# --------------------------------------------------------------------------------------------------------------
                if name_flag == True:
                    name_score += 1
                    for k, v in word_base['commands'].items():
                        if text in v:
                            # name_flag = False
                            # name_score = 0
                            try:
                                getattr(eval(k[0]), k[1])()
                            except AttributeError:
                                print("комманда распознанна, но не имеет функции")

                if name_score == 3:
                    name_score = 0
                    name_flag = False
# --------------------------------------------------------------------------------------------------------------
        except OSError as E:
            print(E)

"хуй"