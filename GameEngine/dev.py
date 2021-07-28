#! /usr/bin/python3.9
import actions
import item_lib
import dbmod
character=dbmod.get_row('name','bob','saves')
choice = ""

while (choice != 'x'):
    print('''What would you like to test?
    1 - arena
    2 - print creature stats
    3 - slay ROUS
    4 - enter the store
    5 - print stats for mouse
    6 - use potion''')

    choice = str(input ('make your selection: '))

    print ('You chose ' +  choice)

    if (choice == '1'):
        actions.wiper()
        actions.arena(character)
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
    elif (choice == '6'):
        actions.use_item(character,'potion')
    elif (choice == 'x'):
        exit()
