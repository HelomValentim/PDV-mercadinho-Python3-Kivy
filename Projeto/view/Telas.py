from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput


class TelaDeLogin(FloatLayout):
    def __init__(self, **kwargs):
        super(TelaDeLogin, self).__init__(**kwargs)

        self.bt = Button(text="Login")
        self.bt.size_hint = 200, 200

        self.add_widget(self.bt)

class TelaPrincipal(App):
    def build(self):
        return TelaDeLogin()