import sqlite3 as lite
import sys


def connect(db='objects.db'):
    con = None
    try:
        con = lite.connect(db)
    except:
        print(lite.Error)
    return con

def test_connection():
    con = connect()
    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')
    data = cur.fetchone()
    print ("SQLite version: %s" % data)
    con.close()

def show_tables():
    con = connect()
    cur = con.cursor()
    cur.execute('SELECT name FROM sqlite_master')
    data = cur.fetchall()
    con.close()
    return (data)

def check_for_table(name):
    con = connect()
    cur = con.cursor()
    cur.execute(f'''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{name}' ''')
    if cur.fetchone()[0]==1:
        return 0
    else:
        return 1
    con.close()

def create_table(name,fields):
    print(f'checking for table: {name}')
    if check_for_table(name) == 1:
        con = connect()
        cur = con.cursor()
        cur.execute(f'create table {name} ({fields})')
        con.close()
        return 0
    else:
        return 1

def delete_table(name):
    if check_for_table(name) == 0:
        con = connect()
        cur = con.cursor()
        cur.execute(f'''DROP TABLE '{name}' ''')
        return 0
    else :
        return 1

def show_fields(table):
    con = connect()
    cur = con.cursor()
    if check_for_table(table) == 0:
        cur.execute(f'''PRAGMA table_info({table})''')
        data = cur.fetchall()
        fields=[]
        for i in data:
            fields.append(i[1])
        return(fields)
    con.close()

def show_table(table):
    con = connect()
    cur = con.cursor()
    if check_for_table(table) == 0:
        cur.execute(f'''SELECT * FROM {table} ''')
        return cur.fetchall()
    con.close()

def add_row(table,fields,values):
    con = connect()
    cur = con.cursor()
    if check_for_table(table) == 0:
        cur.execute(f'''INSERT INTO {table}{fields} VALUES {values}''')
        con.commit()
