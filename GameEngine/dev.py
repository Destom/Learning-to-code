#! /usr/bin/python3.9
import actions
import item_lib
import dbmod

choice = ""

while (choice != 'x'):
    print('''What would you like to test?
    1 - arena
    2 - print creature stats
    3 - slay ROUS
    4 - enter the store''')

    choice = str(input ('make your selection: '))

    print ('You chose ' +  choice)

    if (choice == '1'):
        actions.wiper()
        actions.arena()
    elif (choice == '2'):
        actions.wiper()
        creature = dbmod.get_row('name','mouse','creatures')
        actions.print_status(creature)
    elif (choice == '3'):
        actions.wiper()
        actions.combat_victory(character_lib.ROUS)
    elif (choice == '4'):
        actions.wiper()
        actions.home_store.enter()
    elif (choice == '5'):
        opponent = dbmod.get_row('name','mouse','creatures')
        print(opponent['name'])
    elif (choice == 'x'):
        exit()
