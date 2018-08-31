import sqlite3

class Sql(object):
    def __init__(self):
        self.conn = sqlite3.connect("base.db")

    def testarLoginSenha(self, login, senha):
        return self.conn.execute("select login, senha from usuario where login = '{}' and senha = '{}'".format(login, senha)).fetchall()
