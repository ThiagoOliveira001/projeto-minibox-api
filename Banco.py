import psycopg2

class Banco():
    def __init__(self, host, db, usr, pwd):
        self.__db = psycopg2.connect(host=host, database=db, user=usr, password=pwd)

    def inserir(self, sql):
        print (sql)
        try:
            cur=self.__db.cursor()
            cur.execute(sql)
            cur.close()
            self.__db.commit()
        except:
            return False
        return True
    
    def selecionar(self, sql):
        try:
            cur=self.__db.cursor()
            cur.execute(sql)
            rs=cur.fetchall()
        except:
            return None
        return rs
