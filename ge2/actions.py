import classes
import random

def print_status(character):
    print('name: ' + character.name)
    print('health: ' + str(character.health) + '/' + str(character.max_health))
    print('attack: ' + str(character.attack))
    print('defence: ' + str(character.defence))
    print(f'purse currently holds {character.gold}')
    print(str(character.inventory))
    print('')

def combat_attack(attacker,defender):
    if (attacker.attack > defender.defence):
        defender.health -= (attacker.attack - defender.defence)
    print (str(defender.name) + " health is now " + str(defender.health))

def combat_defence(attacker):
    attacker.defence += 1
    print (str(attacker.name) + " defence is now " + str(attacker.defence))

def combat_victory(opponent):
    wiper()
    print('well done you have vanquished the ' + opponent.name)
    opponent.health = opponent.max_health
    combat_reward = random.choice(opponent.inventory.item_list)
    print (f'for your victory you win {combat_reward}')
    if type(combat_reward) == str:
        inventory_user.item_list.append(combat_reward)
    elif type(combat_reward) == int:
        user.gold += combat_reward

def combat_action(opponent):
    user.attack = user.stat_attack
    user.defence = user.stat_defence
    while (user.health > 0):
        print ("""what would you like to do?
        1 - Attack
        2 - Defend
        3 - Use item""")
        action_choice = str(input("your choice:"))
        if (action_choice == '1'):
            combat_attack(user,opponent)
            if (opponent.health == 0):
                combat_victory(opponent)
                break
        elif (action_choice == '2'):
            combat_defence(user)
        elif (action_choice == '3'):
            select_item()
        print ("The " + str(opponent.name) + " attacks")
        combat_attack(opponent,user)
        if (user.health <= 0):
            print('The ' + opponent.name + ' slayed you. This is the end')

def arena():
    print ('''welcome to the aren, we have many opponents for you to fight.
who would you like to fighh?
    1 - mouse
    2 - Rat
    3 - ROUS''')

    opponent_choice = str(input('please select your opponent: '))

    if (opponent_choice == '1'):
        opponent = mouse
    elif (opponent_choice == '2'):
        opponent = rat
    elif (opponent_choice == '3'):
        opponent = ROUS

    print ("Your opponent is")
    print_status(opponent)
    print ("Your details are")
    print_status(user)
    combat_action(opponent)

def use_item(item_to_use):
    print("You use " +item_to_use.name+ ":")
    user.max_health += item_to_use.max_health_up
    if ((user.max_health - user.health) > item_to_use.health_up):
        user.health +=  item_to_use.health_up
    else:
        user.health = user.max_health
    inventory_user.item_list.remove(item_to_use.name)
    print_status(user)

def select_item():
    print('in your inventory you have:')
    print('(1) ' + str(inventory_user.item_list.count('potion')) + ' potion(s)')
    item_to_use = input('what item would you like to use?:')
    if (item_to_use == '1'):
        if (inventory_user.item_list.count('potion') >0):
            use_item(potion)
        else:
            print("You don't have enough of those")

def wiper():
    for line in range(1,100):
        print('')
