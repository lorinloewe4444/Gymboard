import sqlite3

connection = sqlite3.connect('GymBoard.db')
cursor = connection.cursor()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (10, 'Biologie', 0)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (11, 'BG', 0)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (12, 'Chemie', 0)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (13, 'Chinastudien', 0)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (14, 'Deutsch', 0)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (15, 'Englisch', 0)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (16, 'WR', 0)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (17, 'Französisch', 0)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (18, 'Geschichte', 0)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (19, 'Geografie', 0)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (20, 'Griechisch', 0)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (21, 'Italienisch', 0)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (22, 'Informatik', 0)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (23, 'Latein', 0)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (24, 'Mathematik', 0)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (25, 'Musik', 0)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (26, 'Physik', 0)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (27, 'PAM', 0)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (28, 'PPP', 0)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (29, 'Russisch', 0)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (30, 'Spanisch', 0)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (31, 'Sport', 0)"
cursor.execute(sql)
connection.commit()

#--------------------------------------------------------------------------
# Biologie - 10xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (1010, 'Grundlagenfach', 10)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (1011, 'Schwerpunktfach', 10)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (1012, 'Schwerpunktfach', 10)"
cursor.execute(sql)
connection.commit()

# Biologie - GF - 1010xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (101010, 'Einsprachig', 1010)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (101011, 'Zweisprachig', 1010)"
cursor.execute(sql)
connection.commit()

# Biologie - GF - Einsprachig - 101010xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (10101010, 'Gym 1', 101010)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (10101011, 'Gym 2', 101010)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (10101012, 'Gym 3', 101010)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (10101013, 'Gym 4', 101010)"
cursor.execute(sql)
connection.commit()

# Biologie - GF - Zweisprachig - 101011xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (10101110, 'Gym 1', 101011)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (10101111, 'Gym 2', 101011)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (10101112, 'Gym 3', 101011)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (10101113, 'Gym 4', 101011)"
cursor.execute(sql)
connection.commit()

# Biologie - SF - 1011xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (101110, 'Gym 1', 1011)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (101111, 'Gym 2', 1011)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (101112, 'Gym 3', 1011)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (101113, 'Gym 4', 1011)"
cursor.execute(sql)
connection.commit()

# Biologie - EF - 1012xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (101210, 'Gym 3', 1012)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (101211, 'Gym 4', 1012)"
cursor.execute(sql)
connection.commit()





# BG 11xx
# Chemie 12xx
# Deutsch 14xx
# Englisch 15xx
# WR 16xx
# Französisch 17xx
# Geschichte 18xx
# Geografie 19xx
# Italienisch 21xx
# Informatik 22xx
# Latein 23xx
# Mathematik 24xx
# Musik 25xx
# Physik 26xx
# PAM 27xx
# PPP 28xx
# Sport 31xx


connection.close()
