from kivy.app import App
from kivy.uix.button import Button

class Programa(App):

    def funcaoDeClique(self):
        print("Voce clicou no botão")

    def build(self):
        botao = Button()
        botao.text = "Clique Aqui"
        botao.background_color = (.2, 1, .2, 1)
        botao.size_hint = None, None
        botao.size = 100, 50
        botao.pos_hint = {"x": .7, "y": .5}
        botao.on_press = self.funcaoDeClique
        return botao

tela = Programa()
tela.run()