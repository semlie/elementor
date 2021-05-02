# -*- coding: utf-8 -*-
import sqlite3
import time
from sqlite3 import Error


def create_connection():
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    db_file = 'C:/Users/lieb/PycharmProjects/elemntor/db/sqlite_elemntor.sqlit'

    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_urls(url):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    conn = create_connection()
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM sites where url = ?",(url,))

        rows = cur.fetchall()

        # for row in rows:
        return rows

def _update(q):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    conn = create_connection()
    with conn:
        cur = conn.cursor()
        cur.execute(*q)

    # rows = cur.fetchall()

    # for row in rows:

def update_site(url,risk):
        select= select_urls(url)
        if select:
            id = select[0][0]
            r = 0 if not risk else 1
            row ={"id":id,"url": url, 'risk': r}

            q= ("REPLACE INTO sites values(:id, :url, :risk)", row)
            _update(q)
        else:
            row = { "id":None,"url": url, 'risk': 0}
            q= ("REPLACE INTO sites values( :id,:url, :risk)", row)

            _update( q)

def update_category(url,catDict):
    select =select_urls(url)
    if select:
        id = select[0][0]
        for k,v in catDict.items():
            row = {"urlId": id, "catName": k, 'count': v}
            q = ("REPLACE INTO categories values(:urlId, :catName, :count)", row)
            _update(q)

def logger(url):
    t= int(time.time())
    select = select_urls(url)
    if select:
        id = select[0][0]
        row = {"urlId": id, "lastUpdate":t}
        q = ("REPLACE INTO log values(:urlId, :lastUpdate)", row)
        _update(q)

def select_logger(url_id):
    q = "SELECT urlId, MAX(lastUpdate) FROM  log where urlId =?", (url_id)
    conn = create_connection()
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT urlId, MAX(lastUpdate) FROM  log where urlId =?", (url_id,))
        rows = cur.fetchall()

        # for row in rows:
        return rows[0]

def get_url_id(url):
    select =select_urls(url)
    if select:
        id = select[0][0]
        return id

def select_task_by_priority(conn, priority):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM sites")
    # cur.execute("SELECT * FROM sites WHERE priority=?", (priority,))

    rows = cur.fetchall()

    for row in rows:
        print(row)


def main():

    # create a database connection
    conn = create_connection()
    with conn:
        print("1. Query task by priority:")
        # select_task_by_priority(conn, 1)
        # url = 'www.elementor1.com'
        #
        # update_category(url,{'information technology': 15, 'mobile communications': 4, 'Computer and Internet Info': 1, 'blogs': 1})
        # # print("2. Query all tasks")
        # # select_all_tasks(conn)
        res = select_logger(3)
        print(res)


if __name__ == '__main__':
    main()