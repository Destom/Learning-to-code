#importing sql DB library namming it lite
import sqlite3 as lite

#setting log level
def logging_func(value):
    options = {'debug':0,
        'info':1}
    return options[value]
log_level='debug'
logging = logging_func(log_level)

#commands for gatheing variables
def get_table(table):
    print('Runnign get table command') if logging <= 0 else ''
    if table == 'null':
        print('table value is null running input') if logging <= 0 else ''
        return input('what is the table name? ')
    else:
        print(f'looking for {table}') if logging <= 0 else ''
        return table
def get_fields(fields):
    print('running get fields command') if logging <= 0 else ''
    if fields == 'null':
        print('fileds values are null running input') if logging <= 0 else ''
        return input ('what are the fields(sepperated by a comma)? ')
    else:
        print(f'looking for {fields}') if logging <= 0 else ''
        return fields
def get_values(values):
    print('running get vlaues command') if logging <= 0 else ''
    if values == 'null':
        print('values are null running input') if logging <= 0 else ''
        values = input ('what are the values(sepperated by a comma)? ')
        if "," in values:
            return tuple(values.split(','))
        else:
            returned_values = "('" + values + "')"
            print(f'values will look like {returned_values}') if logging <= 0 else ''
            return returned_values
    else:
        print(f'values will look like {values}') if logging <= 0 else ''
        return values

#initial connections and verificaitons
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
def check_for_table(table = 'null'):
    table = get_table(table)
    con = connect()
    cur = con.cursor()
    command=f'''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{table}' '''
    print(f'checking for table by running command: {command}') if logging <= 0 else ''
    cur.execute(command)
    if cur.fetchone()[0]==1:
        return 0
    else:
        return 1
    con.close()

#Viewing commands
def show_tables():
    print('Getting a list of all tables') if logging <= 0 else ''
    con = connect()
    cur = con.cursor()
    cur.execute('SELECT name FROM sqlite_master')
    data = cur.fetchall()
    con.close()
    return (data)
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

#adding commands
def create_table(table = 'null',fields = 'null'):
    table = get_table(table)
    fields = get_fields(fields)
    if check_for_table(table) == 1:
        con = connect()
        cur = con.cursor()
        command = f'create table {table} ({fields})'
        print(f'table not found creating table with {command}') if logging <= 0 else ''
        cur.execute(command)
        con.close()
        return 0
    else:
        return 1
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
def add_row(table='null',fields='null',values='null'):
    table = get_table(table)
    fields = get_fields(fields)
    values = get_values(values)
    con = connect()
    cur = con.cursor()
    if check_for_table(table) == 0:
        command = f'''INSERT INTO {table} ({fields}) VALUES {values}'''
        print(f'table found adding row with: {command}') if logging <= 0 else ''
        cur.execute(command)
        con.commit()
    con.close()

#Removing commnads
def delete_table(table = 'null'):
    table = get_table(table)
    if check_for_table(table) == 0:
        con = connect()
        cur = con.cursor()
        cur.execute(f'''DROP TABLE '{table}' ''')
        return 0
    else :
        return 1
def drop_row(table='null',fields='null',values='null'):
    table = get_table(table)
    fields = get_fields(fields)
    values = get_values(values)
    values= values.strip('()')
    con = connect()
    cur = con.cursor()
    if check_for_table(table) == 0:
        command = f'''DELETE FROM {table} WHERE {fields} like {values}'''
        print(f'table found dropping row with: {command}') if logging <= 0 else ''
        cur.execute(command)
        con.commit()
    con.close()
