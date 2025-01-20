import pyautogui
import webbrowser
from sys import exit as EXIT
from os import system

class BaseFunction():

    def __init__(self):
        pass

    def music(self):
        pyautogui.press('playpause')

    def prev_music(self):
        pyautogui.press('prevtrack')

    def next_music(self):
        pyautogui.press('nexttrack')

    def param_vol(self):
        system('C:\Windows\explorer.exe ms-settings:apps-volume')

    # def vol_down(self):
    #     pyautogui.press('volumedown')
    #
    # def vol_up(self):
    #     pyautogui.press('volumeup')

    def open_dota(self):
        webbrowser.open("steam://rungameid/570")

    def eexit(self):
        EXIT(7)

    def reload(self):
        raise OSError

    def restart_PC(self):
        system('shutdown /r /t 0')
        EXIT(7)

    def off_PC(self):
        system('shutdown /s /t 0')
        EXIT(7)

    def another(self):
        pass

