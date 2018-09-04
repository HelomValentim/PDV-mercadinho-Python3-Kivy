from Projeto.model.sql import Sql

class Produto(object):
    def __init__(self):
        self.nome = ""
        self.codigo = ""
        self.preco = ""
        self.Sql = Sql()

    def cadastraProduto(self, nome, codigo, preco):
        cadastra = Sql



