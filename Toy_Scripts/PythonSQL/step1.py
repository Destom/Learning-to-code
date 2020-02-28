import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE characters
             (name,max_health,stat_attack,stat_defence,inventory,gold,health,attack,defence)''')

# Insert a row of data
c.execute("INSERT INTO characters VALUES ('bob','10','2','1','item_lib.inventory_user','50','1','1','1')")
c.execute("INSERT INTO characters VALUES ('mouse','2','1','1','item_lib.inventory_gold','50','1','1','1')")
c.execute("INSERT INTO characters VALUES ('rat','10','2','1','item_lib.inventory_basic','50','1','1','1')")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes ha6ve been committed or they will be lost.
conn.close()
