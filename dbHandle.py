#!./env/bin/python3
"""Database Handle"""
import web
import pymysql
import mysql.connector

class DBHandle:

    tables = []
    status = False

    def __init__(self):
        # Pour transaction
        self.webdb = web.database(
            dbn='mysql',
            host='localhost',
            port=3306,
            user='test',
            pw='test',
            db='quentinvinot',
        )

        # Pour créer les tables si nescessaire
        self.mysqlco = mysql.connector.connect(
            host="localhost",
            user="test",
            passwd="test",
            database="quentinvinot",
            auth_plugin="mysql_native_password"
        )

        self.cursor = self.mysqlco.cursor()
        DBHandle.status = self.table_init()


    def check_tables(self):
        self.cursor.execute("SHOW TABLES")

        for x in self.cursor:
            print(x[0])
            DBHandle.tables.append(x[0])
            print(DBHandle.tables)

        if '_etudiants' in DBHandle.tables \
        and '_etudiants' in DBHandle.tables \
        and '_cours' in DBHandle.tables:
            print('tables OK')
        else:
            print('tables not loaded')
            return False
        return True

    def table_init(self):
        if not self.check_tables():
            for line in open('./sql.sql'):
                self.cursor.execute(line)
        return True

    def info_tables(self):
        if DBHandle.status:
            info_tables = [] 
            for x in DBHandle.tables:
                query = "describe " + x
                print(query)
                self.cursor.execute(query)
                print(vars(self.cursor))
                info_tables.append(self.cursor)
        return info_tables


if __name__ == "__main__":
    print('hllo')
    db = DBHandle()
    info = db.info_tables()
    print(vars(info))