from Projeto.model.sql import Sql

class Usuario(object):
    def __init__(self):
        self.nome = ""
        self.senha = ""
        self.login = ""
        self.Sql = Sql()

    def testaLoginSenha(self, login):
        try:
            self.existeLogin = list((self.Sql.testarLoginSenha(login))[0])
        except:
            return 0
        else:
            return 1
