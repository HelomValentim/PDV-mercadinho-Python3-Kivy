from kivy.app import App
from kivy.lang import Builder
from sys import path
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

    def entrarNoSistema(self, login, senha):
        self.usuario = Usuario()
        if (self.usuario.testaLoginSenha(login, senha)):
            App.root.GerenciadorDeTelas.current="Tela1"
        else:
            self.ids.labelMensagemLogin.text = "Login ou senha incorreto"


class TelaInicial(App):
    def build(self):
        self.title = "Ponto De Vendas"
        self.telaDeLogin = TelaDeLogin()

        self.tela1 = Tela1()
        self.tela2 = Tela2()
        self.gerenciador = GerenciadorDeTelas()

        return self.gerenciador


