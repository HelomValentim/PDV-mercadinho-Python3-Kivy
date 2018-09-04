import sqlite3
from sys import path

import sqlite3
from sys import path

class Sql(object):
    def query(self, comando):
        self.conn = sqlite3.connect(path[1]+"/Projeto/model/base.db")
        try:
            retorno = self.conn.execute(comando).fetchall()
            self.conn.commit()
        except:
            self.conn.close()
            return 0
        else:
            self.conn.close()
            return retorno

    def prepareQuery(self, **kwargs):
        tipo = kwargs["tipo"]
        tabela = kwargs["tabela"]
        parametros = kwargs["parametros"]
        filtro = kwargs["filtro"]

        if(tipo == "select"):
            query = "SELECT "
            if len(list(parametros.keys())) > 1:
                for parametro in list(parametros.keys()):
                    query+="{}, ".format(parametro)
            else:
                query+=list(parametros.keys())[0]+" FROM "+tabela
            if len(list(filtro.keys()))>1:
                query += " WHERE {} = '{}'".format(list((filtro.keys()))[0], list(filtro.values())[0])
                for parametro in range(1,len(list(filtro.keys()))):
                    query += " AND {} = '{}'".format(list((filtro.keys()))[parametro], list(filtro.values())[parametro])
            else:
                query+=" WHERE {} = '{}'".format(list(filtro.keys())[0],list(filtro.values())[0])+";"
            return query

        if(tipo == "insert"):
            query = "INSERT INTO {}(".format(tabela)
            if(len(list(parametros.keys()))>1):
                for parametro in list(parametros.keys()):
                    query+="{}, ".format(parametro)
            else:
                query+="{}".format(list(parametros.keys()))
            query+=") values("
            if(len(list(parametros.values()))>1):
                for parametro in list(parametros.values()):
                    query+="{}, ".format(parametro)
                query+=");"
            return  query

    def selectEqual(self, tabela, parametros, filtro):
        return self.query(self.prepareQuery(tipo = "select", tabela = tabela, parametros = parametros, filtro = filtro))

    def deleteEqual(self, tabela, filtro):
        return self.query(self.prepareQuery("delete", tabela, filtro))


    def insertEqual(self, tabela, parametros, filtro):
        return self.query(self.prepareQuery("insert", tabela, parametros, filtro))

    def updateEqual(self, tabela, parametros, filtro):
        raw_query = "UPDATE '{}' SET '{}' = '{}' WHERE '{}' = '{}'".format(tabela, parametros.keys(),
                                                                           parametros.values(), filtro.keys(), filtro.values())
        return self.query(self.prepareQuery("update", tabela, parametros, filtro))

    def select(self, tabela):
        raw_query = "SELECT * FROM '{}'".format(tabela)
        return self.query(raw_query)







