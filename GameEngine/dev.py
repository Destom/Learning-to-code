#! /usr/bin/python3.9
import actions
import item_lib
import dbmod
#character=dbmod.get_row('name','bob','saves')
#character['items'] = character['items'].split(',')
character = actions.load_being('bob','saves')
choice = ""

while (choice != 'x'):
    print('''What would you like to test?
    1 - arena
    2 - print Character stats
    3 - slay ROUS
    4 - enter the store
    5 - print stats for mouse
    6 - use item
    0 - Load character''')

    choice = str(input ('make your selection: '))
    actions.wiper()
    print ('You chose ' +  choice)

    if (choice == '1'):
        actions.arena(character)
    elif (choice == '2'):
        creature = dbmod.get_row('name','mouse','creatures')
        actions.print_status(character)
    elif (choice == '3'):
        actions.combat_victory(character['name'],actions.load_being('ROUS','creatures'))
    elif (choice == '4'):
        actions.home_store.enter()
    elif (choice == '5'):
        opponent = dbmod.get_row('name','mouse','creatures')
        print(opponent['name'])
    elif (choice == '6'):
        item_choice = actions.get_item(character['items'])
        actions.use_item(character,item_choice)
        actions.remove_item(character,item_choice)
    elif (choice == '9'):
        pass
    elif (choice == '0'):
        character=dbmod.get_row('name','bob','saves')
        character['items'] = character['items'].split(',')
    elif (choice == 'x'):
        exit()
