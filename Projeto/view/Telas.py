from Projeto.model.usuario import Usuario
from Projeto.model.produto import Produto

from kivy.app import App
from kivy.lang import Builder

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.stacklayout import StackLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.config import Config
from kivy.core.window import Window

#desabilita o multi touch que cria bolas vermelhas na tela
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

#define as configurações da tela
Window.size = (1024, 720)
#desabilita o redimensionamento
Config.set('graphics', 'resizable', False)
#definimos as posições iniciais da janela
Config.set('graphics', 'position', 'custom')
Config.set('graphics', 'left', 0)
Config.set('graphics', 'top',  0)

#classe que gerencia as janelas
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
        if (self.usuario.logar(login, senha)):
            self.gerenciador.current = "TelaSistema"
        else:
            self.root.get_screen("TelaDeLogin").ids.labelMensagemLogin.text = "Login ou senha invalidos"

    def abrirTelaVender(self):
        self.root.get_screen("TelaSistema").remove_widget(self.root.get_screen("TelaSistema").ids.botoesTelas)
        self.root.get_screen("TelaSistema").add_widget(self.root.get_screen("TelaVendas"))
    def voltarTelaVender(self):
        self.root.get_screen("TelaSistema").remove_widget(self.root.get_screen("TelaVendas"))
        self.root.get_screen("TelaSistema").add_widget(self.root.get_screen("TelaSistema").ids.botoesTelas)
    def abrirTelaProdutos(self):
        self.root.get_screen("TelaSistema").remove_widget(self.root.get_screen("TelaSistema").ids.botoesTelas)
        self.root.get_screen("TelaSistema").add_widget(self.root.get_screen("TelaProdutos"))
    def voltarTelaProdutos(self):
        self.root.get_screen("TelaSistema").remove_widget(self.root.get_screen("TelaProdutos"))
        self.root.get_screen("TelaSistema").add_widget(self.root.get_screen("TelaSistema").ids.botoesTelas)

    def cadastraProduto(self, nome, codigo, preco):
        self.produto = Produto()