from kivy.app import App
from kivy.uix.button import Button

class Programa(App):

    def funcaoDeClique(self):
        print(self.entrada.text)

    def build(self):
        self.botao = Button()
        self.botao.text = "Clique Aqui"
        self.botao.background_color = (.2, 1, .2, 1)
        self.botao.size_hint = None, None
        self.botao.size = 100, 50
        self.botao.pos_hint = {"x": .7, "y": .5}
        self.botao.on_press = self.funcaoDeClique
        return self.botao

tela = Programa()
tela.run()