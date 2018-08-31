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


class TelaDeLogin(Screen):
    pass


class TelaInicial(App):
    def build(self):
        self.title = "Ponto De Vendas"
        self.gerenciador = GerenciadorDeTelas()
        self.telaDeLogin = TelaDeLogin()
        self.tela1 = Tela1()

        self.gerenciador.add_widget(self.tela1)
        self.gerenciador.add_widget(self.telaDeLogin)

        return self.gerenciador

    def entrarNoSistema(self, login, senha):
        self.usuario = Usuario()
        if (self.usuario.testaLoginSenha(login, senha)):
            self.gerenciador.current="Tela1"
        else:
            self.root.get_screen('TelaDeLogin').ids.labelMensagemLogin.text = "Login ou senha invalidos"

