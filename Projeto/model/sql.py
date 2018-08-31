import sqlite3
from sys import path

class Sql(object):
    def __init__(self):
        self.conn = sqlite3.connect(path[1]+"/Projeto/model/base.db")

    def testarLoginSenha(self, login, senha):
        return self.conn.execute("select login, senha from usuario where login = '{}' and senha = '{}'".format(login, senha)).fetchall()
