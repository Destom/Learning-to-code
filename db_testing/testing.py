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
    7) add fields
    8) test get_values
    x) exit the test lab
    Please make your selection: ''')
    if choice == '1':
        print (dbmod.check_for_table())
    elif choice == '2':
        print(dbmod.show_tables())
    elif choice == '3':
        print(dbmod.create_table())
    elif choice == '4':
        print(dbmod.delete_table())
    elif choice == '5':
        dbmod.view_table()
    elif choice == '6':
        dbmod.add_row('batman','this,another','value1,value2')
    elif choice == '7':
        print(dbmod.add_fields('batman', 'anotherone'))
    elif choice == '8':
        print(dbmod.get_values('null'))
    elif choice == 'x':
        pass
