import dbmod
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
                self.store_buy()
            elif (store_choice == '2'):
                print(f'''I currently have {self.gold} gold.
                what would you like to sell?''' )

     def store_buy(self):
        print(f'''I currently have {self.inventory.item_list}
            you have {character_lib.user.gold}
            what would you like to buy?''')
        store_purchase_choice = str(input('Your choice: '))
        if self.inventory.item_list.count(store_purchase_choice) > 0:
            print('I have one of those')
            self.inventory.item_list.remove(store_purchase_choice)
            print(f'''my new inventory is {self.inventory.item_list}''')
            item_lib.inventory_user.item_list.append(store_purchase_choice)

home_store = store('home store',item_lib.inventory_lots,50)

def print_status(character):
    print('name: ' + character['name'])
    print('health: ' + str(character['health']))
    print('attack: ' + str(character['attack']))
    print('defence: ' + str(character['defence']))
    print('')

def load_being(name,location):
    temp = dbmod.get_row('name',name,location)
    temp['items'] = temp['items'].split(',')
    return temp

def arena(character):
    choices = {}
    count = 0
    for creature in dbmod.get_field_values(table ='creatures',fields ='name'):
        count+=1
        choices[count] = creature
    print('Creatures available for the arena')
    for item in choices:
        print(f'{item}:{choices[item]}')
    opponent_choice_number = int(input('please select your opponent number: '))
    opponent = choices[opponent_choice_number]
    opponent = load_being(opponent,'creatures')


    print ("Your opponent is")
    print_status(opponent)
    print ("Your details are")
    print_status(character)
    combat_action(character,opponent)

def wiper():
                for line in range(1,100):
                    print('')

######## ITEMS ########
def use_item(being,item):
    item = dbmod.get_row('name',item,'items')
    print(f'''{being['name']} used {item['name']}:''')
    if ((being['max_'+item['increase']] - being[item['increase']]) > item['increase_value']):
        being[item['increase']] += item['increase_value']
    else:
        being[item['increase']] = being['max_'+item['increase']]
    print_status(being)
def get_item(item_list):
    item_dict = {}
    print('items in your inventory')
    for item in item_list:
        if item in item_dict.keys():
            item_dict[item] += 1
        else:
            item_dict[item] = 1
    for item in item_dict:
        print(f'{item}: {str(item_dict[item])}')
    item_to_use = input('what item would you like to use?:')
    return item_to_use
def get_random_item(item_list):
    pass
remove_item = lambda being , item: being['items'].remove(item)

######## Combat ########
def combat_attack(attacker,defender):
    if (attacker['attack'] > defender['defence']):
        defender['health'] = int(defender['health'])
        defender['health'] -= (int(attacker['attack']) - int(defender['defence']))
    print (str(defender['name']) + " health is now " + str(defender['health']))
def combat_defence(attacker):
    attacker['defence'] += 1
    print ((attacker['name']) + " defence is now " + str(attacker['defence']))
def combat_victory(victor,opponent):
    wiper()
    print('well done you have vanquished the ' + opponent['name'])
    #combat_reward = opponent['items']
    combat_reward = random.choice(opponent['items'])
    print (f'for your victory you win {combat_reward}')
    print (f"{victor['items']}")
    victor['items'].append(combat_reward)
def combat_action(character,opponent):
    while (int(character['health']) > 0):
        print ("""what would you like to do?
        1 - Attack
        2 - Defend
        3 - Use item""")
        action_choice = str(input("your choice:"))
        if (action_choice == '1'):
            combat_attack(character,opponent)
            if (opponent['health'] == 0):
                combat_victory(opponent)
                break
        elif (action_choice == '2'):
            combat_defence(character)
        elif (action_choice == '3'):
            item = get_item(character['items'])
            use_item(character,item)
        print ("The " + opponent['name'] + " attacks")
        combat_attack(opponent,character)
        if (character['health'] <= 0):
            print('The ' + opponent['name'] + ' slayed you. This is the end')
