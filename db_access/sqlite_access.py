import sqlite3

# Connect to the local SQLite file
conn = sqlite3.connect('../db.sqlite3')

cur = conn.cursor()

# Fetch unposted furniture
cur.execute("SELECT id, title, description FROM marketplace_furniture WHERE is_posted = 0;")
rows = cur.fetchall()

for row in rows:
    id, title, description = row
    # Post to Kleinanzeigen here
    print(f"Posting: {title}")
    
    # After posting, mark as posted
    cur.execute("UPDATE marketplace_furniture SET is_posted = 1 WHERE id = ?;", (id,))
    conn.commit()

cur.close()
conn.close()