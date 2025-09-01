import pyautogui
import webbrowser
from sys import exit as EXIT
from os import system
from Base.Record import Record
from keyboard import write


class BaseFunction(Record):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def music(self, key='playpause', **kwargs):
        pyautogui.press(key)

    def insert_request(self, **kwargs):
        text = self.merge_text(self.listen_one_msg())
        write(text)
        pyautogui.press('enter')

    def search_youtube(self, **kwargs):
        text = self.merge_text(self.listen_one_msg())
        text = text.replace(" ", "+")
        webbrowser.open_new_tab(rf"https://www.youtube.com/results?search_query={text}")

    def param_vol(self, **kwargs):
        system('C:\Windows\explorer.exe ms-settings:apps-volume')

    # def vol_down(self):
    #     pyautogui.press('volumedown')
    #
    # def vol_up(self):
    #     pyautogui.press('volumeup')

    def open_dota(self, **kwargs):
        webbrowser.open("steam://rungameid/570")

    def eexit(self, **kwargs):
        EXIT(7)

    def reload(self, **kwargs):
        raise OSError

    def restart_PC(self, **kwargs):
        system('shutdown /r /t 0')
        EXIT(7)

    def off_PC(self, **kwargs):
        system('shutdown /s /t 0')
        EXIT(7)

    def another(self, **kwargs):
        pass

