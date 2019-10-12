import character_lib
import item_lib
import random

class store:
     def __init__(self,name,inventory,gold):
        self.name = name
        self.inventory = inventory
        self.gold = gold

     def enter(self):
        store_choice = 0
        print(f'''welcome to {self.name}
we currently have {self.inventory.item_list} in stock.
I have {self.gold} gold if you would like to sell anything to me''')
        while  (store_choice != '3'):
            print ('''What would you like to do
    1 - Buy
    2 - sell
    3 - Leave''')
            store_choice = str(input('Your choice: '))
            if (store_choice == '1'):
                print(f'''I currently have
{self.inventory.item_list}
what would you like to buy?''')
                store_purchase_choice = str(input('Your choice: '))
            elif (store_choice == '2'):
                print(f'''I currently have {self.gold} gold.
                what would you like to sell?''' )




home_store = store('home store',item_lib.inventory_basic,50)

def print_status(character):
    print('name: ' + character.name)
    print('health: ' + str(character.health) + '/' + str(character.max_health))
    print('attack: ' + str(character.attack))
    print('defence: ' + str(character.defence))
    print(f'your purse currently holds {character.gold}')
    print(str(character.inventory.item_list))
    for item in (character.inventory.item_list):
        print (item)
    print('')

def combat_attack(attacker,defender):
    if (attacker.attack > defender.defence):
        defender.health -= (attacker.attack - defender.defence)
    print (str(defender.name) + " health is now " + str(defender.health))

def combat_defence(attacker):
    attacker.defence += 1
    print (str(attacker.name) + " defence is now " + str(attacker.defence))

def combat_victory(opponent):
    print('well done you have vanquished the ' + opponent.name)
    opponent.health = opponent.max_health
    combat_reward = random.choice(opponent.inventory.item_list)
    print (f'for your victory you win {combat_reward}')
    character_lib.item_lib.inventory_user.item_list.append(combat_reward)

def combat_action(opponent):
    character_lib.user.attack = character_lib.user.stat_attack
    character_lib.user.defence = character_lib.user.stat_defence
    while (character_lib.user.health > 0):
        print ("""what would you like to do?
        1 - Attack
        2 - Defend
        3 - Use item""")
        action_choice = str(input("your choice:"))
        if (action_choice == '1'):
            combat_attack(character_lib.user,opponent)
            if (opponent.health == 0):
                combat_victory(opponent)
                break
        elif (action_choice == '2'):
            combat_defence(character_lib.user)
        elif (action_choice == '3'):
            select_item()
        print ("The " + str(opponent.name) + " attacks")
        combat_attack(opponent,character_lib.user)
        if (character_lib.user.health <= 0):
            print('The ' + opponent.name + ' slayed you. This is the end')

def arena():
    print ('''welcome to the aren, we have many opponents for you to fight.
who would you like to fighh?
    1 - mouse
    2 - Rat
    3 - ROUS''')

    opponent_choice = str(input('please select your opponent: '))

    if (opponent_choice == '1'):
        opponent = character_lib.mouse
    elif (opponent_choice == '2'):
        opponent = character_lib.rat
    elif (opponent_choice == '3'):
        opponent = character_lib.ROUS

    print ("Your opponent is")
    print_status(opponent)
    print ("Your details are")
    print_status(character_lib.user)
    combat_action(opponent)

def use_item(item_to_use):
    print("You use " +item_to_use.name+ ":")
    character_lib.user.max_health += item_to_use.max_health_up
    if ((character_lib.user.max_health - character_lib.user.health) > item_to_use.health_up):
        character_lib.user.health +=  item_to_use.health_up
    else:
        character_lib.user.health = character_lib.user.max_health
    character_lib.inventory.remove(item_to_use.name)
    print_status(character_lib.user)

def select_item():
    print('in your inventory you have:')
    print('(1) ' + str(character_lib.inventory.count('potion')) + ' potion(s)')
    item_to_use = input('what item would you like to use?:')
    if (item_to_use == '1'):
        if (character_lib.inventory.count('potion') >0):
            use_item(item_lib.potion)
        else:
            print("You don't have enough of those")
