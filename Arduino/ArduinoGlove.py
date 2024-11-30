import serial
from threading import Thread
from time import sleep
from BaseFunction import *

def listen_port():
    try:
        with serial.Serial('COM4', 9600) as ser:
            print("Ардуино модуль найден")
            while True:
                response = ser.read(5).decode('utf-8')
                if response == "10000":
                    music()
                elif response == "01000":
                    prev_music()
                elif response == "00100":
                    next_music()
                elif response == "00010":
                    vol_down()
                elif response == "00001":
                    vol_up()
    except:
        print("Ардуино модуль не найден")


if __name__ == "__main__":
    Thread(target=listen_port, daemon=False).start()
