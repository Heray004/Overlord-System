from Base.Recognition import Recognition, Thread
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
        conn, cursor = self.sql_connect()
        try:
            while True:
                data = self.get_voice(conn=conn, cursor=cursor)
                if data and data[0][2] == "fifine":
                    print(data)
                    self.executed(conn=conn, cursor=cursor, voice_id=data[0][0])
                    self.last_id = data[0][0]
        except:
            self.sql_close(conn=conn, cursor=cursor)
            exit(7)
        # while True:
        #     try:
        #         self.recognition_start()
        #         print('Система "Overlord" готова к работе')
        #         for text in self.listen():
        #             print(f'>>> {text}')
        #             text = self.merge_text(text)
        #             print(f'>>> {text}')
        #             self.model_recognition(text)
        #     except OSError as E:
        #         print(E)


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
    Over = Overlord(devices=devices)
    Over.cycle()
