# -*- coding: utf-8 -*-
import sqlite3


class DB():
    def __init__(self):
        self.conn =self.create_connection()
    def create_connection(self):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        db_file = 'C:/Users/lieb/PycharmProjects/elemntor/db/sqlite_elemntor.sqlit'
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except sqlite3.Error as e:
            print(e)

        return conn

    def _execute(self,sql_query):
        cur = self.conn.cursor()
        cur.execute(sql_query)

        return cur

    def _select(self,sql_select):
        cur = self._execute(sql_select)
        rows = cur.fetchall()
        for row in rows:
            return  row

    def update(self,sql_update):
        # cursor.execute("insert into foo values(:alpha, :beta, :gamma)", {'alpha': 1, 'beta': 2, 'gamma': 'three'})
        cur = self._execute(sql_update)

    def _insertOrUpdateSite(self,obj):

        cur = self._execute(obj)

    def insertOrUpdateSite(self,row):
        select = self.select(row['url'])
        sqlObj =("REPLACE INTO sites values(:url, :risk)",row)

        self._insertOrUpdateSite(sqlObj)
