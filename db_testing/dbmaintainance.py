import dbmod

choice=''

print('''welcome to the maintanance environment''')
print(dbmod.log_level)
while choice != 'x':
    choice = input('''
    1) Show Tables
    2) View table
    3) show CSV
    4) Create table from CSV
    5) view defaults
    6)
    7)
    8)
    9)
    x) exit the test lab
    Please make your selection: ''')
    if choice == '1':
        print(dbmod.show_tables())
    elif choice == '2':
        print(dbmod.view_table())
    elif choice == '3':
        dbmod.print_csv()
    elif choice == '4':
        dbmod.create_table_from_csv()
    elif choice == '5':
        dbmod.get_row('name','default', 'monsters')
    elif choice == '6':
        pass
    elif choice == '7':
        pass
    elif choice == '8':
        pass
    elif choice == '9':
        pass
    elif choice == 'x':
        pass
