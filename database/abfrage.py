import sqlite3

con = sqlite3.connect('GymBoard.db')
cur = connection.cursor()

sql = "SELECT * FROM users"
cur.execute(sql)
for dsatz in cursor:
    print(dsatz)

# Matthias

con.close()
