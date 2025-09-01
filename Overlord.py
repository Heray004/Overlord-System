from Base.Recognition import Recognition, Thread
# from kivy.app import App
# from kivy.uix.screenmanager import ScreenManager
# from kivy.core.window import Window
# from Ui.Ui_test import Login
# from Ui.String import *


class Overlord(Recognition):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cycle()


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
    Overlord(devices=devices)
