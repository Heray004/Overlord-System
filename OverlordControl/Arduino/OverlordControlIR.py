import serial


class OverlordControlIR:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def OverlordControl_IR_start(self):
        try:
            self.ser = serial.Serial('COM4', 9600, dsrdtr=0)
            print("Overlord Control IR готов к работе")
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
