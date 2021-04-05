import dbmod

choice=''

print('''welcome to the test environment, please select your test''')

while choice != 'x':
    choice = input('''
    1) test the db connection
    2) show table list
    3) Create table
    x) exit the test lab
    Please make your selection: ''')
    if choice == '1':
        dbmod.test_connection()
    elif choice == '2':
        dbmod.show_tables()
    elif choice == '3':
        table = input('what is the table name? ')
        fields = input ('what are the fields(sepperated by a comma)? ')
        dbmod.create_table(table,fields)
    elif choice == 'x':
        pass
