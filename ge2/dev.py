#! /usr/bin/python3.7
import actions
import classes


#items
potion = classes.item('potion',10,0,5)
super_potion = classes.item('super_potion',20,0,10)

#Inventories
inventory_user = classes.inventory('character_inventory',["potion"])
inventory_basic = classes.inventory("inventory_basic",['potion'])
inventory_advanced = classes.inventory("inventory_advanced",['potion','super_potion'])
inventory_lots = classes.inventory("inventory_lots",['potion','potion','potion','potion','super_potion','super_potion','super_potion','super_potion'])
inventory_gold = classes.inventory("inventory_gold",[50])

#Characters
user = classes.character('bob',10,2,1,inventory_user,50)
mouse =  classes.character('mouse',2,1,1,inventory_gold)
rat =  classes.character('rat',10,2,1,inventory_basic)
ROUS =  classes.character('ROUS',15,4,1,inventory_advanced)

#Stores
home_store =  classes.store('home store',inventory_lots,50)


choice = ""

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
        actions.arena()
    elif (choice == '2'):
        actions.wiper()
        actions.print_status(user)
    elif (choice == '3'):
        actions.wiper()
        actions.combat_victory(ROUS)
    elif (choice == '4'):
        actions.wiper()
        actions.home_store.enter()
    elif (choice == 'x'):
        exit()
