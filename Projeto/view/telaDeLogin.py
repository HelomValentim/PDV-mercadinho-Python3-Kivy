from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput

class TelaDeLogin(FloatLayout):
    def __init__(self, **kwargs):
        super(TelaDeLogin, self).__init__(**kwargs)
        self.labelNome = Label(text="Login", size_hint=(None, None), pos_hint={"x": .25, "y": .65}, font_size=30)
        self.entradaNome = TextInput(size_hint=(None, None), size=(400, 40), pos_hint={"x": .4, "y": .7})
        self.labelSenha = Label(text="Senha", size_hint = (None, None), pos_hint={"x": .25, "y": .55}, font_size = 30)
        self.entradaSenha = TextInput(size_hint = (None, None), size = (400, 40), pos_hint={"x": .4, "y": .6})
        self.botaoEntrar = Button(text="Entrar", size_hint = (None, None), size=(150, 50), pos_hint={"x": .713, "y": .5})
        self.labelMensagemLogin = Label(text="", size_hint=(None, None), pos_hint={"x": .25, "y": .3}, font_size=30)


        self.add_widget(self.labelNome)
        self.add_widget(self.entradaNome)
        self.add_widget(self.labelSenha)
        self.add_widget(self.entradaSenha)
        self.add_widget(self.botaoEntrar)
        self.add_widget(self.labelMensagemLogin)


from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout

class gerenciador(ScreenManager):
    def __init__(self):
        Tela1(Screen)
        Tela2(Screen)

class Tela1(FloatLayout):
    FloatLayout:
        Button:
            text: "Tela1"
            #root.current faz referencia a tela atual
            on_press: app.root.current = 'tela2'

class JanelaApp(App):
    def build(self):
        return gerenciador()


class Tela1(FloatLayout):
    #telas nao tem ids tem nomes
    FloatLayout:
        Button:
            text: "Tela2"
            #root.current faz referencia a tela atual
            on_press: app.root.current = 'tela1'
