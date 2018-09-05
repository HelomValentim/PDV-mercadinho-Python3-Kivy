from Projeto.model.sql import Sql

class Produto(object):
    def __init__(self):
        self.nome = ""
        self.codigo = ""
        self.preco = ""
        self.sql = Sql()

    def cadastraProduto(self, nome, codigo, preco):
        #devemos verificar varias condições antes de executar essa query, coloquei sem os testes apenas na fase beta
        return self.sql.insertEqual("produto", {"nome": nome,"codigo": codigo, "preco": preco}, {"":""})

    def listarProdutos(self):
        return self.sql.select("produto")

    def buscarProduto(self, codigo):
        try:
            return self.sql.selectEqual("produto", {"nome": "nome", "preco": "preco"}, {"codigo": int(codigo)})
        except:
            pass