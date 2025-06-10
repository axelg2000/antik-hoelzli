


import sqlite3

# Use ../ to go one folder up
conn = sqlite3.connect('antik_hoelzli/db.sqlite3')

cur = conn.cursor()

cur.execute("SELECT id, title, age, price, dimensions, description FROM marketplace_furniture;")
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()