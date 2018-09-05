import sqlite3
from sys import path

import sqlite3
from sys import path

class Sql(object):
    def query(self, comando):
        """esse metodo executa as queryes apos elas serem preparadas no metodo
        prepareQuery, tambem podemos passar queryes prontas que elas serão executadas aqui"""
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
            if retorno == [('',)]:
                return 1
            else:
                return retorno

    def prepareQuery(self, **kwargs):
        """essa função prepara a query para ser executada
        verificando os parametros e definindo suas posições
        outras verificações devem ser feitas nos seus respectivos objetos antes de
        serem de ser executado os metodos dessa classe aqui
        """

        #parametros da query
        tipo = kwargs["tipo"]
        tabela = kwargs["tabela"]
        parametros = kwargs["parametros"]
        filtro = kwargs["filtro"]

        #verificamos o tipo da query
        if(tipo == "select"):
            #criamos a query
            raw_query = "SELECT "
            if len(list(parametros.keys())) > 1:
                #verificamos as quantidades de parametros passados e concatemanos as chaves na query
                for parametro in list(parametros.keys()):
                    raw_query+="{}, ".format(parametro)
                raw_query = raw_query[:-2]
            else:
                #caso seja passado apenas um parametro para a query caimos nessa condição
                raw_query+="{}".format(list(parametros.keys())[0])
            raw_query+=" FROM "+tabela

            #verificamos as quantidades de parametros de filtro passados e concatemanos os valores de filtro na query
            if len(list(filtro.keys()))>1:
                raw_query += " WHERE {} = '{}'".format(list((filtro.keys()))[0], list(filtro.values())[0])
                for parametro in range(1,len(list(filtro.keys()))):
                    raw_query += " AND {} = '{}'".format(list((filtro.keys()))[parametro], list(filtro.values())[parametro])
            else:
                #caso seja passado apenas um valor para o filtro a query caimos nessa condição
                raw_query+=" WHERE {} = '{}'".format(list(filtro.keys())[0],list(filtro.values())[0])+";"
            return raw_query

        #o funcionamento dessa condição é semelhante a de cima
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







