from Ui.String import *


class Login(Screen):
    def __init__(self, App, **kwargs):
        super().__init__()
        self.App = App
        self.name = 'Login'
        self.login_layout = FloatLayout()
        self.add_widget(self.login_layout)

        self.back = Button(
            text='',
            size_hint=(None, None),
            size=(600, 600),
            pos_hint={'center_x': .5, 'center_y': .8},
            background_color=btn_dark_grey,
            color=main_color2
        )
        self.login_layout.add_widget(self.back)

        self.login = TextInput(
            multiline=False,
            size_hint=(None, None),
            size=(400, 40),
            pos_hint={'center_x': .5, 'center_y': .9},
            text="admin",
        )
        self.login_layout.add_widget(self.login)
        self.password = TextInput(
            password=True,
            multiline=False,
            size_hint=(None, None),
            size=(400, 40),
            pos_hint={'center_x': .5, 'center_y': .7},
        )
        self.login_layout.add_widget(self.password)

        # Button
        self.Go_app = Button(
            text='Login',
            size_hint=(None, None),
            size=(100, 40),
            pos_hint={'center_x': .5, 'center_y': .2},
            background_color=btn_dark_grey,
            color=main_color2
        )
        self.Go_app.bind(on_press=self.on_press)
        self.login_layout.add_widget(self.Go_app)

        self.log = Label(
            text='Login',
            font_size="20sp",
            size_hint=(.35, .05),
            pos_hint={'center_x': .5, 'center_y': .6},
            color=green
        )
        self.login_layout.add_widget(self.log)

    def on_press(self, *args):
        self.devices_name = ["fifine", "Webcam"]  # , "Petlya"]
        self.App.on_stop()

