import sqlite3 as lite
import sys

con = None

def test_connection():
    print('testing connection')
    con = lite.connect('objects.db') 
    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')
    data = cur.fetchone()
    print ("SQLite version: %s" % data)
    con.close()

def show_tables():
    print('attempting to list tables')
    con = lite.connect('objects.db')
    cur = con.cursor()
    cur.execute('SHOW TABLES')

def create_table(name,fields):
    print(f'creating table: {name}')
    print(f'Creating fileds: {fields}')
    con = lite.connect('objects.db')
    cur = con.cursor()
    cur.execute(f'create table {name} ({fields})')
    con.close()
