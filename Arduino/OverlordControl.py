import serial
class OverlordControl():
    def __init__(self):
        pass
        # try:
        #     self.ser = serial.Serial('COM4', 9600, dsrdtr=0)
        #     print("Overlord Control готов к работе (__init__)")
        # except:
        #     print("Ардуино модуль не найден (__init__)")

    def search_com(self):
        try:
            self.ser = serial.Serial('COM4', 9600, dsrdtr=0)
            print("Overlord Control готов к работе (search_com)")
            return self.ser
        except:
            print("Ардуино модуль не найден (search_com)")

    def off_conditioner(self):
        try:
            self.ser.write(b'10')
        except:
            print("Ардуино модуль не найден")

    def set17(self):
        try:
            self.ser.write(b'17')
        except:
            print("Ардуино модуль не найден")

    def set18(self):
        try:
            self.ser.write(b'18')
        except:
            print("Ардуино модуль не найден")

    def vol_down(self):
        try:
            self.ser.write(b'--')
        except:
            print("Ардуино модуль не найден (vol_down)")

    def vol_up(self):
        try:
            self.ser.write(b'++')
        except:
            print("Ардуино модуль не найден (vol_up)")



if __name__ == "__main__":
    # Thread(target=listen_port, daemon=False).start()
    pass
