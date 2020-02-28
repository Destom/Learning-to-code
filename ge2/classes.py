class character:
    def __init__(self,name,max_health,stat_attack,stat_defence,inventory,gold=0,health=1,attack=1,defence=1):
        self.name = name
        self.max_health = max_health
        self.stat_attack = stat_attack
        self.stat_defence = stat_defence
        self.inventory = inventory
        self.gold = gold
        self.health = max_health
        self.attack = stat_attack
        self.defence = stat_defence

class item:
    def __init__(self,name,value,max_health_up,health_up):
        self.name = name
        self.value = value
        self.max_health_up = max_health_up
        self.health_up = health_up

class inventory:
    def __init__(self,name,item_list):
        self.name = name
        self.item_list = item_list

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

class item:
    def __init__(self,name,value,max_health_up,health_up):
        self.name = name
        self.value = value
        self.max_health_up = max_health_up
        self.health_up = health_up

class inventory:
    def __init__(self,name,item_list):
        self.name = name
        self.item_list = item_list
