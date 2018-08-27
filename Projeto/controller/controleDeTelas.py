from Projeto.controller.telaInicial import TelaInicial

class controleTelaInicial():
    def __init__(self):
        self.telaInicial = TelaInicial()

    def iniciaSistema(self):
        self.telaInicial.run()