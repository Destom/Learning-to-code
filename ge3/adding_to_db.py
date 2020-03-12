import csv
import dbconn

#defaults
def defaults():
    global name
    global health
    global stat_attack
    global stat_defence
    global inventory
    global gold
    global max_health
    global attack
    global defence
    name='def_name'
    health = 10
    stat_attack = 2
    stat_defence = 1
    inventory = "def_inventory"
    gold = 10
    max_health = 10
    attack = 2
    defence = 1
defaults()
hollow = ('def_name',10,2,1,'def_inventory',10,10,2,1)

def choose(stat):
    #return(f'Current {stat} is ' + eval(stat))
    stat = input('what would you like the name to be? ')

with open('characters.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are: \n{", ".join(row)}')
            line_count += 1
        else:
            item_number = 0
            for idx, item in enumerate(row):
                if item == '':
                    item = hollow[idx]
                    print('its empty')
                    print (hollow[idx])
                    print (item)
            print(row)
            line_count += 1
            defaults()
    print(f'Processed {line_count} lines.')


'''
choice =''
while choice != 'x':
    print(f"""current stats are set to
    1) Name: '{name}'
    2) Health: {health}
    3) Attack: {attack}
    4) Defence: {defence}
    5) Inventory: '{inventory}'
    6) Gold: {gold}
    7) Max Health: {max_health}
    8) Stat Attack: {stat_attack}
    9) Stat Defence{stat_defence})
    e) to add current character to DB
    x) exit""")
    choice = str(input('what would you like to do? '))
    if choice == 'e':
        c.execute(f"INSERT INTO {table} VALUES ('{name}',{health},{attack},{defence},'{inventory}',{gold},{max_health},{stat_attack},{stat_defence})")
    elif choice == '1':
        print(choose('name'))
        print(name)
        name = input('what would you like the name to be? ')
'''
