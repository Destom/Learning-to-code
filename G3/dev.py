import characters
import actions
import combat

#inventories
character_inventory={'potion':1}
inventory_gold={'gold':50}
inventory_basic={'potion':1}
inventory_advanced={'potion':3,'super_potion':1}

#Characters
user = characters.character('bob',10,2,1,character_inventory,50)
mouse =  characters.character('mouse',2,1,1,inventory_gold)
rat =  characters.character('rat',10,2,1,inventory_basic)
ROUS =  characters.character('ROUS',15,4,1,inventory_advanced)
print(rat.name)
choice=''
while (choice != 'x'):
    print('''What would you like to test?
    1 - arena
    2 - print character stats
    3 - slay ROUS
    4 - enter the store''')

    choice = str(input ('make your selection: '))

    print ('You chose ' +  choice)

    if (choice == '1'):
        actions.wiper()
        combat.arena()
    elif (choice == '2'):
        actions.wiper()
        print(actions.print_status(user))
    elif (choice == '3'):
        actions.wiper()
        actions.combat_victory(ROUS)
    elif (choice == '4'):
        actions.wiper()
        actions.home_store.enter()
    elif (choice == 'x'):
        exit()
