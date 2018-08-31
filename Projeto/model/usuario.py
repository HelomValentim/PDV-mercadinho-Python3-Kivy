from Projeto.model.sql import Sql

class Usuario(object):
    def __init__(self):
        self.nome = ""
        self.senha = ""
        self.login = ""
        self.Sql = Sql()

    def testaLoginSenha(self, login, senha):
        try:
            self.existe = list((self.Sql.testarLoginSenha(login, senha))[0])
        except:
            return 0
        else:
            return 1


