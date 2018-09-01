from Projeto.model.usuario import Usuario

from kivy.app import App
from kivy.lang import Builder

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from kivy.uix.stacklayout import StackLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
from kivy.core.window import Window
Window.size = (1024, 720)

class GerenciadorDeTelas(ScreenManager):
    pass

class TelaFramePrincipal(Screen):
    pass

class TelaSistema(Screen):
    pass

class TelaVendas(Screen):
    pass

class TelaDeLogin(Screen):
    pass

class TelaProdutos(Screen):
    pass

class TelaCadastroProduto(Screen):
    pass

class Telas(App):
    def build(self):
        self.title = "Ponto De Vendas"
        self.gerenciador = GerenciadorDeTelas()

        self.telaDeLogin = TelaDeLogin()
        self.TelaSistema = TelaSistema()
        self.TelaVendas = TelaVendas()
        self.TelaProdutos = TelaProdutos()
        self.TelaCadastroProduto = TelaCadastroProduto()
        return self.gerenciador

    def entrarNoSistema(self, login, senha):
        self.usuario = Usuario()
        if (self.usuario.testaLoginSenha(login, senha)):
            self.gerenciador.current = "TelaSistema"
        else:
            self.root.get_screen("TelaDeLogin").ids.labelMensagemLogin.text = "Login ou senha invalidos"
            
    def abrirTelaVender(self):
        self.root.get_screen("TelaSistema").remove_widget(self.root.get_screen("TelaSistema").ids.botoesTelas)
        self.root.get_screen("TelaSistema").add_widget(self.root.get_screen("TelaVendas"))
    def voltarTelaVender(self):
        self.root.get_screen("TelaSistema").remove_widget(self.root.get_screen("TelaVendas"))
        self.root.get_screen("TelaSistema").add_widget(self.root.get_screen("TelaSistema").ids.botoesTelas)
