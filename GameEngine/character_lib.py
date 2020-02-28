import item_lib

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


user = character('bob',10,2,1,item_lib.inventory_user,50)

mouse = character('mouse',2,1,1,item_lib.inventory_gold)
rat = character('rat',10,2,1,item_lib.inventory_basic)
ROUS = character('ROUS',15,4,1,item_lib.inventory_advanced)
