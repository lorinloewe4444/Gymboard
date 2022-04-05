import sqlite3

connection = sqlite3.connect('GymBoard.db')
cursor = connection.cursor()

sql = "SELECT * FROM users"
cursor.execute(sql)
for dsatz in cursor:
    print(dsatz)

connection.close()
