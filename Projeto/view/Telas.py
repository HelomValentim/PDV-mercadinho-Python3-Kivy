from kivy.app import App
from Projeto.model.usuario import Usuario
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen

class GerenciadorDeTelas(ScreenManager):
    pass

class Tela1(Screen):
    pass

class Tela2(Screen):
    pass

class TelaDeLogin(Screen):
    def __init__(self):
        super(TelaDeLogin, self)
        self.ids.botaoEntrar.on_press = self.entrarNoSistema()

    def entrarNoSistema(self):
        print("entrou")


class TelaInicial(App):
    def build(self):
        self.title = "Ponto De Vendas"
        self.telaLogin = TelaDeLogin()
        self.tela1 = Tela1()
        self.tela2 = Tela2()
        self.gerenciador = GerenciadorDeTelas()
        return self.gerenciador

