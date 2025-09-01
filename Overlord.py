from Base.Recognition import Recognition, Thread
#from kivy.app import App
# from kivy.uix.screenmanager import ScreenManager
# from kivy.core.window import Window
# from Ui.Ui_test import Login
# from Ui.String import *


class Overlord(Recognition):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # cycle = Thread(target=self.cycle, daemon=True)
        # cycle.start()
        self.cycle()

    def cycle(self):
        model_flag = None
        while True:
            print('Использовать модель?')
            while model_flag is None:
                text = self.listen_one_msg()
                if 'да' in text:
                    model_flag = 1
                    print('Система распознавания: модель')
                elif 'нет' in text:
                    model_flag = 0
                    print('Система распознавания: словарь')

            try:
                self.recognition_start(model_flag=model_flag)
                print('Система "Overlord" готова к работе')
                if model_flag == 0:
                    for text in self.listen():
                        print(f'>>> {text}')
                        text = self.merge_text(text)
                        print(f'>>> {text}')
                        self.list_recognition(text)
                elif model_flag == 1:
                    for text in self.listen():
                        print(f'>>> {text}')
                        text = self.merge_text(text)
                        print(f'>>> {text}')
                        self.model_recognition(text)

            except OSError as E:
                print(E)

    # def build(self):
    #     self.title = "Overlord"
    #     sm.add_widget(Login(kwargs=sm))
    #     return sm


if __name__ == "__main__":
    devices = {}
    devices_name = ["fifine", "Webcam"]  # , "Petlya"]
    for i in devices_name:
        devices[i] = [None, None, None]
    # Window.clearcolor = main_color1
    # sm = ScreenManager()
    Overlord(devices=devices)
