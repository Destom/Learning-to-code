import csv
import sqlite3
conn = sqlite3.connect('objects.db')
c = conn.cursor()

#defaults
def defaults():
    global table
    global name
    global health
    global stat_attack
    global stat_defence
    global inventory
    global gold
    global max_health
    global attack
    global defence
    table='characters'
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


def choose(stat):
    #return(f'Current {stat} is ' + eval(stat))
    stat = input('what would you like the name to be? ')
"""
try:
    print(f'trying to find table: {table}')
    c.execute(f'select * FROM {table}')
    print('Why I no find table')
except:
    c.execute(f'''CREATE TABLE {table}
            (name,health,attack,defence,inventory,gold,max_health,stat_attack,stat_defence)''')
    print(f'{table}')"""

with open('characters.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            name = row[0]
            health = row[1]
            attack = row[2]
            defence = row[3]
            inventory = row[4]
            if row[5] !='':
                gold = row[5]
            max_health = row[6]
            stat_attack = row[7]
            stat_defence = row[8]
            print(f'1) Name: {name}\n'
                f'2) Health: {health}\n'
                f'3) Attack: {attack}\n'
                f'4) Defence: {defence}\n'
                f'5) Inventory: {inventory}\n'
                f'6) Gold: {gold}\n'
                f'7) Max Health: {max_health}\n'
                f'8) Stat Attack: {stat_attack}\n'
                f'9) Stat Defence{stat_defence})\n')
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


#Save and close
conn.commit()
conn.close()
