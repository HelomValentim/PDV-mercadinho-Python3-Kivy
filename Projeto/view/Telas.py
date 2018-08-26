from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput


class TelaDeLogin(FloatLayout):
    def __init__(self, **kwargs):
        super(TelaDeLogin, self).__init__(**kwargs)
        self.labelNome = Label(text="Login")
        self.labelNome.size_hint = None, None
        self.labelNome.pos_hint = {"x": .25, "y": .65}
        self.labelNome.font_size = 30

        self.entradaNome = TextInput()
        self.entradaNome.size_hint = None, None
        self.entradaNome.size = 400, 40
        self.entradaNome.pos_hint = {"x": .4, "y": .7}

        self.labelSenha = Label(text="Senha")
        self.labelSenha.size_hint = None, None
        self.labelSenha.pos_hint = {"x": .25, "y": .55}
        self.labelSenha.font_size = 30

        self.entradaSenha = TextInput()
        self.entradaSenha.size_hint = None, None
        self.entradaSenha.size = 400, 40
        self.entradaSenha.pos_hint = {"x": .4, "y": .6}


        self.botaoEntrar = Button(text="Entrar")
        self.botaoEntrar.size_hint = None, None
        self.botaoEntrar.size = 150, 50
        self.botaoEntrar.pos_hint = {"x": .713, "y": .5}
        self.botaoEntrar.on_press = self.entrarNoSistema

        self.add_widget(self.labelNome)
        self.add_widget(self.entradaNome)
        self.add_widget(self.labelSenha)
        self.add_widget(self.entradaSenha)
        self.add_widget(self.botaoEntrar)

    def entrarNoSistema(self):
        if(self.entradaNome.text == "walter" and self.entradaSenha.text == "1234"):
            print("entrou")
        else:
            print("não entrou")

class TelaPrincipal(App):
    def build(self):
        return TelaDeLogin()