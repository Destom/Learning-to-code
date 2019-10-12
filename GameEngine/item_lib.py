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

potion = item('potion',10,0,5)
super_potion = item('super_potion',20,0,10)

inventory_user = inventory('character_inventory',["potion"])
inventory_basic = inventory("inventory_basic",['potion'])
inventory_advanced = inventory("inventory_advanced",['potion','super_potion'])
inventory_lots = inventory("inventory_lots",['potion','potion','potion','potion','super_potion','super_potion','super_potion','super_potion'])
inventory_gold = inventory("inventory_gold",[50])
