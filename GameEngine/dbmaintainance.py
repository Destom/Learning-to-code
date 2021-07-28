import dbmod

choice=''

print('''welcome to the maintanance environment''')
print(dbmod.log_level)
while choice != 'x':
    choice = input('''
    1) Show Tables
    2) View table
    3) Show CSV
    4) Create table from CSV
    5) delete table
    6) Recreate table
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
        dbmod.delete_table()
    elif choice == '6':
        csv_choice = dbmod.choose_csv()
        dbmod.delete_table(csv_choice.removesuffix('.csv'))
        dbmod.create_table_from_csv(csv_choice)
    elif choice == '7':
        pass
    elif choice == '8':
        pass
    elif choice == '9':
        pass
    elif choice == 'x':
        pass
