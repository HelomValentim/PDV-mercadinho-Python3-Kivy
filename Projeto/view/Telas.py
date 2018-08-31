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
    pass
    # def entrarNoSistema(self):
    #     print("entrou")
    #     self.usuario = Usuario()
    #     if (self.usuario.testaLoginSenha(self.ids.entradaLogin.text, self.ids.entradaSenha.text)):
    #         App.root_window.
    #     else:
    #         self.ids.labelMensagemLogin.text = "Login regeitado"




class TelaInicial(App):
    def build(self):
        self.title = "Ponto De Vendas"
        self.telaLogin = TelaDeLogin()
        self.tela1 = Tela1()
        self.tela2 = Tela2()
        self.gerenciador = GerenciadorDeTelas()
        return self.gerenciador