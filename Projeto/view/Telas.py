from Projeto.model.usuario import Usuario
from Projeto.model.produto import Produto

from kivy.app import App
from kivy.lang import Builder

from kivy.uix.listview import ListItemLabel
from kivy.adapters.simplelistadapter import SimpleListAdapter

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

class TelaUsuarios(Screen):
    pass

class TelaTabelaProdutosListar(Screen):
    pass

class Telas(App):
    def build(self):
        self.title = "Ponto De Vendas"

        self.usuario = Usuario()
        self.listaDeUsuarios = self.usuario.listarUsuarios()

        self.produto = Produto()
        self.listaDeProdutos = self.produto.listarProdutos()

        self.produtosSendoVendidos = []

        self.gerenciador = GerenciadorDeTelas()
        self.telaDeLogin = TelaDeLogin()
        self.TelaSistema = TelaSistema()
        self.TelaVendas = TelaVendas()
        self.TelaProdutos = TelaProdutos()
        self.TelaCadastroProduto = TelaCadastroProduto()
        self.TelaUsuarios = TelaUsuarios()
        self.TelaTabelaProdutosListar = TelaTabelaProdutosListar()
        self.totalVenda = 0
        return self.gerenciador

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
    def abrirTelaUsuarios(self):
        self.root.get_screen("TelaSistema").remove_widget(self.root.get_screen("TelaSistema").ids.botoesTelas)
        self.root.get_screen("TelaSistema").add_widget(self.root.get_screen("TelaUsuarios"))

    def voltarTelaUsuarios(self):
        self.root.get_screen("TelaSistema").remove_widget(self.root.get_screen("TelaUsuarios"))
        self.root.get_screen("TelaSistema").add_widget(self.root.get_screen("TelaSistema").ids.botoesTelas)

    def cadastraProduto(self, nome, codigo, preco):
        self.produto = Produto()
        retorno = self.produto.cadastraProduto(nome, codigo, preco)
        if retorno == 0:
            self.root.get_screen("TelaProdutos").ids.labelMensagemCadastroDeProdutos.text = "ERRO AO CADASTRAR"
        else:
            self.root.get_screen("TelaProdutos").ids.labelMensagemCadastroDeProdutos.text = "CADASTRO EFETUADO!"

    def cadastraUsuario(self, login, nome, senha):
        self.usuario = Usuario()
        retorno = self.usuario.cadastrar(login, senha, nome)
        if retorno == 0:
            self.root.get_screen("TelaUsuarios").ids.labelMensagemCadastroDeUsuarios.text = "ERRO AO CADASTRAR"
        else:
            self.root.get_screen("TelaUsuarios").ids.labelMensagemCadastroDeUsuarios.text = "CADASTRO EFETUADO!"

    def entrarNoSistema(self):
        self.gerenciador.current = "TelaSistema"

    def adicionarProdutoVenda(self, codigoDoProduto):
        if(codigoDoProduto!=""):
            produto = (str((self.produto.buscarProduto(codigoDoProduto)))[2:-2]).split(",")
            produtoStr = "Nome: {} Preço: {}".format(produto[0][1:-1], produto[1])
            self.root.get_screen("TelaVendas").ids.ProdutosSendoVendidos.add_widget(Label(text=produtoStr, size_hint=(
                None, None), size=(1000, 33), font_size=20))
            self.totalVenda += float(produto[1])
            self.root.get_screen("TelaVendas").ids.labelValorTotal.text = "Total: {:.2f}".format(self.totalVenda)
