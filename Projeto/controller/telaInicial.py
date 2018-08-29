from kivy.app import App
from Projeto.view.telaDeLogin import TelaDeLogin
from Projeto.view.telaDeLogin import Tela1
from Projeto.view.telaDeLogin import Tela2
from Projeto.view.telaDeLogin import gerenciador
from Projeto.model.usuario import Usuario

class TelaInicial(App):
    def build(self):
        self.title = "Janela de login"
        self.icon = "icone.png"
        self.telaDeLogin = TelaDeLogin()
        self.tela1 = Tela1()
        self.tela2 = Tela2()
        self.gerenciador = gerenciador()

        self.telaDeLogin.botaoEntrar.on_press = self.entrarNoSistema
        return self.telaDeLogin

    def entrarNoSistema(self):
        self.usuario = Usuario()
        if(self.usuario.testaLoginSenha(self.telaDeLogin.entradaNome.text)):
            self.telaDeLogin.labelMensagemLogin.text = "Login aceito"
        else:
            self.telaDeLogin.labelMensagemLogin.text = "Login regeitado"


        #        return gerenciador()
