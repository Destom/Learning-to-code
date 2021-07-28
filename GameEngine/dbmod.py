db_location='./data_files/objects.db'
csv_location='./data_files'
#importing sql DB library namming it lite
import sqlite3 as lite
#importing commands to use with fiels
import csv
from os import listdir

#setting log level
def logging_func(value):
    options = {'debug':0,
        'info':1}
    return options[value]
log_level='info'
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
def connect_one(db=db_location):
    con = None
    try:
        con = lite.connect(db)
        con.row_factory = lite.Row
    except:
        print(lite.Error)
    return con
def connect_many(db=db_location):
    con = None
    try:
        con = lite.connect(db)
    except:
        print(lite.Error)
    return con
def test_connection():
    con = connect_many()
    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')
    data = cur.fetchone()
    print ("SQLite version: %s" % data)
    con.close()
def check_for_table(table = 'null'):
    table = get_table(table)
    con = connect_many()
    cur = con.cursor()
    command=f'''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{table}' '''
    print(f'checking for table by running command: {command}') if logging <= 0 else ''
    cur.execute(command)
    if cur.fetchone()[0]==1:
        return 0
        print(f'found table: {table}') if logging <= 0 else ''
    else:
        print(f'did not find table: {table}') if logging <= 0 else ''
        return 1
    con.close()

#Viewing commands
def show_tables():
    print('Getting a list of all tables') if logging <= 0 else ''
    con = connect_many()
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
    con = connect_many()
    cur = con.cursor()
    if check_for_table(table) == 0:
        cur.execute(f'''SELECT * FROM {table} ''')
        return cur.fetchall()
    con.close()
def get_field_values(table = 'null', fields = 'null'):
    print(f'Running get single column command') if logging <= 0 else ''
    table = get_table(table)
    con = connect_many()
    cur = con.cursor()
    if check_for_table(table) == 0:
        command  = f'''SELECT {fields} FROM {table}; '''
        print(f'Running command: {fields}') if logging <= 0 else ''
        cur.execute(command)
        data=cur.fetchall()
        list = []
        for row in data:
            if row[0] != 'default':
                list.append(row[0])
        return list
def show_fields(table = 'null'):
    table = get_table(table)
    con = connect_many()
    cur = con.cursor()
    if check_for_table(table) == 0:
        cur.execute(f'''PRAGMA table_info({table})''')
        data = cur.fetchall()
        fields=[]
        for i in data:
            fields.append(i[0])
        return(fields)
    con.close()
def get_row(field, value, table = 'null'):
    print(f'Running get row command') if logging <= 0 else ''
    table = get_table(table)
    con = connect_one()
    cur = con.cursor()
    if check_for_table(table) == 0:
        command  = f'''SELECT * FROM {table} WHERE {field}="{value}"; '''
        print(f'Running command: {command}') if logging <= 0 else ''
        cur.execute(command)
        data=cur.fetchone()
        print(f'Data pulled from table: {data[0:]}') if logging <= 0 else ''
        data = dict(data)
        for item in data:
            try:
                data[item] = int(data[item])
            except:
                pass
        return data

#adding commands
def create_table(table = 'null',fields = 'null'):
    print(f'Running create table command') if logging <= 0 else ''
    table = get_table(table)
    fields = get_fields(fields)
    if check_for_table(table) == 1:
        con = connect_many()
        cur = con.cursor()
        command = f'create table {table} ({fields})'
        print(f'table not found creating table with {command}') if logging <= 0 else ''
        cur.execute(command)
        con.close()
        return 0
    else:
        print(f'table {table} found not creating') if logging <= 0 else ''
        return 1
def add_fields(table = 'null',fields = 'null'):
    table = get_table(table)
    fields = get_fields(fields)
    fields = list(fields.split(','))
    con = connect_many()
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
    con = connect_many()
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
        con = connect_many()
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
    con = connect_many()
    cur = con.cursor()
    if check_for_table(table) == 0:
        command = f'''DELETE FROM {table} WHERE {fields} like {values}'''
        print(f'table found dropping row with: {command}') if logging <= 0 else ''
        cur.execute(command)
        con.commit()
    con.close()

#CSV commands
def get_csvs():
    folder_list = (listdir(csv_location))
    csv_list = [ item for item in folder_list if item[-4:]=='.csv']
    return csv_list
def choose_csv():
    csv_dict={}
    count = 0
    for csv in get_csvs():
        count += 1
        file = csv.removesuffix('.csv')
        csv_dict[count]=file
    print('files available for import:')
    for item in csv_dict:
        print(f'''{item}:{csv_dict[item]}''')
    print(f'Current csv_dict is {csv_dict}') if logging <= 0 else ''
    result = (csv_dict[int(input('''pick your item(by number): '''))])+'.csv'
    print(f'file chosen {result}') if logging <= 0 else ''
    return result
def open_csv(file='null', returning='null'):
    if file == 'null':
        file=choose_csv()
    if returning == 'null':
        returning = input('do you want (f)ields or (r)ows?: ')[0].lower()
        print(f'returning value currently {returning}') if logging <= 0 else ''
    with open(f'{csv_location}/{file}', 'r') as file:
        csvreader = csv.reader(file)
        fields = next(file).strip()
        if returning == 'f':
            print(f'returning fields {fields}') if logging <= 0 else ''
            return fields
        elif returning == 'r':
            results = []
            for row in csvreader:
                results.append(row)
            return results
def print_csv(file='null'):
    file = choose_csv()
    print(open_csv(file,'f'))
    for row in open_csv(file,'r'):
        print(row)
def get_default(file='null'):
    if file == 'null':
        file = choose_csv()
    table_name = file.removesuffix('.csv')
    fields = open_csv(file, returning='f')
    rows = open_csv(file, returning='r')
    print(f'value for file: {file}') if logging <= 0 else ''
    print(f'value for table_name: {table_name}') if logging <= 0 else ''
    print(f'value for fields: {fields}') if logging <= 0 else ''
    print(f'value for rows: {rows}') if logging <= 0 else ''
    print(f'Looking for defaults') if logging <= 0 else ''
    defaults = [row for row in rows if row[0] == 'default'][0]
    print(f'value for defaults: {defaults}') if logging <= 0 else ''
    return defaults


#the big ones
def create_table_from_csv(file='null'):
    if file == 'null':
        file = choose_csv()
    table_name = file.removesuffix('.csv')
    fields = open_csv(file, returning='f')
    rows = open_csv(file, returning='r')
    defaults = get_default (file=file)
    print(f'value for file: {file}') if logging <= 0 else ''
    print(f'value for table_name: {table_name}') if logging <= 0 else ''
    print(f'value for fields: {fields}') if logging <= 0 else ''
    print(f'value for rows: {rows}') if logging <= 0 else ''
    create_table(table=table_name,fields=fields)
    for row in rows:
        count=0
        for item in row:
            if item == '':
                row[count] = defaults[count]
                print(f'value for item: {row[count]}') if logging <= 0 else ''
            count += 1
        print(f'value for row: {row}') if logging <= 0 else ''
        row = tuple(row)
        print(f'value for row after tuple command: {row}') if logging <= 0 else ''
        add_row(table_name,fields,row)
