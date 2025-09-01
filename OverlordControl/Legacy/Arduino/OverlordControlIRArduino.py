import serial


class OverlordControlIRArduino:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def overlord_control_ir_start(self):
        try:
            self.ser = serial.Serial('COM4', 9600, dsrdtr=0)
            print("Overlord Control IR готов к работе")
            return self.ser
        except:
            print("Ардуино модуль не найден (search_com)")

    def conditioner_off(self):
        try:
            self.ser.write(b'10')
            return "Successfully conditioner_off"
        except:
            print("Ардуино модуль не найден")
            return "Ардуино модуль не найден"

    def set17(self):
        try:
            self.ser.write(b'17')
            return "Successfully set17"
        except:
            print("Ардуино модуль не найден")
            return "Ардуино модуль не найден"

    def set18(self):
        try:
            self.ser.write(b'18')
        except:
            print("Ардуино модуль не найден")

    def vol_down(self):
        try:
            self.ser.write(b'--')
            return "Successfully vol_down"
        except:
            print("Ардуино модуль не найден")
            return "Ардуино модуль не найден"

    def vol_up(self):
        try:
            self.ser.write(b'++')
            return "Successfully vol_up"
        except:
            print("Ардуино модуль не найден")
            return "Ардуино модуль не найден"
