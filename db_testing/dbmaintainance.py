import dbmod


choice=''

print('''welcome to the maintanance environment''')
print(dbmod.log_level)
while choice != 'x':
    choice = input('''
    1) Show Tables
    2) Show options
    3) Create table from file
    4)
    5)
    6)
    7)
    8)
    9)
    x) exit the test lab
    Please make your selection: ''')
    if choice == '1':
        print(dbmod.show_tables())
    elif choice == '2':
        print(dbmod.get_csvs())
    elif choice == '3':
        print(dbmod.open_csv())
    elif choice == '4':
        dbmod.choose_csv()
    elif choice == '5':
        pass
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
