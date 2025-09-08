from Base.Recognition import Recognition, Thread
from time import sleep
# from kivy.app import App
# from kivy.uix.screenmanager import ScreenManager
# from kivy.core.window import Window
# from Ui.Ui_test import Login
# from Ui.String import *


class Overlord(Recognition):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.last_id = 0

    def cycle(self):

            while True:
                data = self.get_voice()
                if data and data[0][2] == "fifine":
                    print(data)
                    self.executed(voice_id=data[0][0])
                    self.last_id = data[0][0]
                elif data and data[0][2] != "fifine":
                    print(data)
                    self.deny(voice_id=data[0][0])
                sleep(0.1)


# class Ui(App, Screen):
#     def build(self):
#         self.title = "Overlord"
#         sm.add_widget(Login(App=self))
#         return sm
#
#     def on_stop(self):
#         Window.close()


if __name__ == "__main__":
    # Window.clearcolor = main_color1
    # sm = ScreenManager()
    # Ui().run()
    devices = {}
    devices_name = ["fifine", "Webcam"]  # , "Petlya"]
    # devices_name = Login.devices_name
    for i in devices_name:
        devices[i] = [None, None, None]
    Over = Overlord()  # devices=devices
    Over.cycle()
