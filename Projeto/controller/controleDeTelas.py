from Projeto.view.Telas import *

class TelaInicial(App):
    def build(self):
        self.telaLogin = TelaDeLogin()
        self.tela1 = Tela1()
        self.tela2 = Tela2()
        self.gerenciador = GerenciadorDeTelas()
        return self.gerenciador
    
    def iniciaSistema(self):
        self.run()