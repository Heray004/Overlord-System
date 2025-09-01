from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
#from kivy_garden.graph import Graph, MeshLinePlot
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from kivy.uix.dropdown import DropDown

from kivy.graphics import Color, Rectangle
#from kivy.garden.matplotlib import FigureCanvasKivyAgg
from kivy.uix.boxlayout import BoxLayout
from functools import partial

from datetime import datetime, timedelta
from threading import Thread
import random
import matplotlib.pyplot as plt
import json
import socket
import requests
from dateutil import parser
from matplotlib.dates import DateFormatter, MinuteLocator

red = (255 / 255, 67 / 255, 67 / 255)
white = (255 / 255, 255 / 255, 255 / 255)
white_HEX = "#ffffff"
green = (0 / 255, 158 / 255, 60 / 255)
black = (0/255, 0/255, 0/255, 1)
main_color1 = (0/255, 130/255, 166/255, 1)
main_color1_HEX = "#0082a6"
#main_color2 = (0/255, 183/255, 212/255, 1)
main_color2 = (40/255, 223/255, 252/255, 1)
main_color2_HEX = "#00b7d4"
btn_dark_grey = (150/255, 150/255, 150/255, 1)
btn_dark_grey_HEX = "#969696"
dark_grey = (90/255, 90/255, 90/255, 1)
dark_grey_HEX = "#4c4c4c"
textinput_grey = (200/255, 200/255, 200/255, 1)

size = 838860800
port = 9080
host = "192.168.0.10"
global_host = "178.140.8.204"
url = "http://192.168.0.10:9080"
global_url = "http://178.140.8.204:9080"
