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
    def clicar(self):
        print("clicado")
        self.current = "Tela1"

class Tela1(Screen):
    pass


class Tela2(Screen):
    pass

class TelaDeLogin(Screen):
    pass

class TelaInicial(App):
    def build(self):
        self.title = "Ponto De Vendas"
        self.telaDeLogin = TelaDeLogin()

        self.tela1 = Tela1()
        self.tela2 = Tela2()
        self.gerenciador = GerenciadorDeTelas()

        #self.telaPrincipal = Builder.load_file(path[1]+"/Projeto/view/telainicial.kv")
        return self.gerenciador


