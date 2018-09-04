import sqlite3
from sys import path

import sqlite3
from sys import path

class Sql(object):
    def query(self, comando):
        self.conn = sqlite3.connect(path[1]+"/Projeto/model/base.db")
        self.cursor = self.conn.cursor()
        try:
            retorno = self.cursor.execute(comando).fetchall()
        except:
            self.conn.close()
            return 0
        else:
            self.conn.commit()
            self.conn.close()
            return retorno

    def prepareQuery(self, **kwargs):
        tipo = kwargs["tipo"]
        tabela = kwargs["tabela"]
        parametros = kwargs["parametros"]
        filtro = kwargs["filtro"]

        if(tipo == "select"):
            raw_query = "SELECT "
            if len(list(parametros.keys())) > 1:
                for parametro in list(parametros.keys()):
                    raw_query+="{}, ".format(parametro)
            else:
                raw_query+=list(parametros.keys())[0]+" FROM "+tabela
            if len(list(filtro.keys()))>1:
                raw_query += " WHERE {} = '{}'".format(list((filtro.keys()))[0], list(filtro.values())[0])
                for parametro in range(1,len(list(filtro.keys()))):
                    raw_query += " AND {} = '{}'".format(list((filtro.keys()))[parametro], list(filtro.values())[parametro])
            else:
                raw_query+=" WHERE {} = '{}'".format(list(filtro.keys())[0],list(filtro.values())[0])+";"
            return raw_query

        if(tipo == "insert"):
            raw_query = "INSERT INTO {}(".format(tabela)
            if(len(list(parametros.keys()))>1):
                for parametro in list(parametros.keys()):
                    raw_query+="{}, ".format(parametro)
            else:
                raw_query+="{}".format(list(parametros.keys()))
            raw_query = raw_query[:-2]
            raw_query+=") values("
            if(len(list(parametros.values()))>1):
                for parametro in list(parametros.values()):
                    raw_query+="'{}', ".format(parametro)
                raw_query = raw_query[:-2]
            else:
                raw_query+="'{}'".format(list(parametros.values())[0])
            raw_query+=");"
            return raw_query

    def selectEqual(self, tabela, parametros, filtro):
        return self.query(self.prepareQuery(tipo="select", tabela = tabela, parametros = parametros, filtro = filtro))

    def insertEqual(self, tabela, parametros, filtro):
        return self.query(self.prepareQuery(tipo="insert", tabela=tabela, parametros=parametros, filtro=filtro))

    def deleteEqual(self, tabela, filtro):
        return self.query(self.prepareQuery("delete", tabela, filtro))

    def updateEqual(self, tabela, parametros, filtro):
        raw_query = "UPDATE '{}' SET '{}' = '{}' WHERE '{}' = '{}'".format(tabela, parametros.keys(),
                                                                           parametros.values(), filtro.keys(), filtro.values())
        return self.query(self.prepareQuery("update", tabela, parametros, filtro))

    def select(self, tabela):
        raw_query = "SELECT * FROM '{}'".format(tabela)
        return self.query(raw_query)







