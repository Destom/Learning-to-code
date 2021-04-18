import sqlite3 as lite
import sys

def get_table(table):
    if table == 'null':
        return input('what is the table name? ')
    else:
        return table
def get_fields(fields):
    if fields == 'null':
        return input ('what are the fields(sepperated by a comma)? ')
    else:
        return fields
def get_values(values):
    if values == 'null':
        values = input ('what are the values(sepperated by a comma)? ')
        return tuple(values.split(','))
    else:
        return values

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

def check_for_table(table = 'null'):
    table = get_table(table)
    con = connect()
    cur = con.cursor()
    cur.execute(f'''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{table}' ''')
    if cur.fetchone()[0]==1:
        return 0
    else:
        return 1
    con.close()

def create_table(table = 'null',fields = 'null'):
    table = get_table(table)
    fields = get_fields(fields)
    if check_for_table(table) == 1:
        con = connect()
        cur = con.cursor()
        cur.execute(f'create table {table} ({fields})')
        con.close()
        return 0
    else:
        return 1

def delete_table(table = 'null'):
    table = get_table(table)
    if check_for_table(table) == 0:
        con = connect()
        cur = con.cursor()
        cur.execute(f'''DROP TABLE '{table}' ''')
        return 0
    else :
        return 1

def show_fields(table = 'null'):
    table = get_table(table)
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

def view_table(table='null'):
    table = get_table(table)
    print(show_fields(table))
    for row in get_table_contents(table):
        print(row)

def get_table_contents(table = 'null'):
    table = get_table(table)
    con = connect()
    cur = con.cursor()
    if check_for_table(table) == 0:
        cur.execute(f'''SELECT * FROM {table} ''')
        return cur.fetchall()
    con.close()

def add_row(table='null',fields='null',values='null'):
    table = get_table(table)
    fields = get_fields(fields)
    values = get_values(values)
    if type(values)!=tuple:
        values=tuple(values.split(','))
    con = connect()
    cur = con.cursor()
    if check_for_table(table) == 0:
        command = f'''INSERT INTO {table} ({fields}) VALUES {values}'''
        print(command)
        cur.execute(command)
        con.commit()
    con.close()

def add_fields(table = 'null',fields = 'null'):
    table = get_table(table)
    fields = get_fields(fields)
    fields = list(fields.split(','))
    con = connect()
    cur = con.cursor()
    if check_for_table(table) == 0:
        for field in fields:
            cur.execute(f'''ALTER TABLE {table} Add [{field}]''')
            con.commit()
        return 0
    con.close()

def drop_row(table='null',fields='null',values='null'):
    table = get_table(table)
    fields = get_fields(fields)
    values = get_values(values)
    con = connect()
    cur = con.cursor()
    if check_for_table(table) == 0:
        command = f'''INSERT INTO {table} ({fields}) VALUES {values}'''
        print(command)
        cur.execute(command)
        con.commit()
    con.close()
