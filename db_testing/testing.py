import dbmod

choice=''

print('''welcome to the test environment, please select your test''')

while choice != 'x':
    choice = input('''
    1) Find table
    2) Show table list
    3) Create table
    4) Remove table
    5) View table
    6) add data
    x) exit the test lab
    Please make your selection: ''')
    if choice == '1':
        table = input('what is the table name? ')
        print (dbmod.check_for_table(table))
    elif choice == '2':
        print(dbmod.show_tables())
    elif choice == '3':
        table = input('what is the table name? ')
        fields = input ('what are the fields(sepperated by a comma)? ')
        print(dbmod.create_table(table,fields))
    elif choice == '4':
        table = input('what table do you want to remove? ')
        print(dbmod.delete_table(table))
    elif choice == '5':
        table = input('what table would you like to invesitgate? ')
        print(dbmod.show_fields(table))
        print(dbmod.show_table(table))
    elif choice == '6':
        dbmod.add_row('batman','(this,that)', ('baterang','grappeling-hook'))
    elif choice == 'x':
        pass
