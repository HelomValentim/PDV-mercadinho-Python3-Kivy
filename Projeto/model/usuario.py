from Projeto.model.sql import Sql

class Usuario(object):
    def __init__(self):
        self.nome = ""
        self.senha = ""
        self.login = ""
        self.sql = Sql()

    def logar(self, login, senha):
        if(self.sql.selectEqual("usuario", {"login": login}, {"login": login, "senha": senha})):
            return 1
        else:
            return 0

    def cadastrar(self, login, senha, nome):
        if(self.sql.insertEqual("usuario", {"login": login,"nome": nome, "senha": senha}, {"":""})):
            return 1
        else:
            return 0