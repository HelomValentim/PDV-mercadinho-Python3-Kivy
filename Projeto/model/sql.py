import sqlite3

class Sql(object):
    def __init__(self):
        self.conn = sqlite3.connect("base.db")

    def testarLoginSenha(self, login):
        return self.conn.execute("select login, senha from usuario where login = '{}'".format(login)).fetchall()
