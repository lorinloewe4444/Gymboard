import sqlite3

connection = sqlite3.connect('GymBoard.db')
cursor = connection.cursor()

# -- user
sql = "INSERT INTO users(eMail, nickName, status, role, datum) VALUES('asterix.gallien@stud.gyminterlaken.ch', 'asterix', 0, 0, '1651587175')"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO users(eMail, nickName, status, role, datum) VALUES('idefix.gallien@stud.gyminterlaken.ch', 'idefix', 1, 1, '1651587175')"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO users(eMail, nickName, status, role, datum) VALUES('obelix.gallien@stud.gyminterlaken.ch', 'obelix', 1, 1, '1651587175')"
cursor.execute(sql)
connection.commit()

# -- document
sql = "INSERT INTO documents(id_User, name, path, datum, id_Tags) VALUES(1, 'firstDocument', 'path1', '1092941466', 1010)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO documents(id_User, name, path, datum, id_Tags) VALUES(3, 'secondDocument', 'path2', '1092941466', 101010)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO documents(id_User, name, path, datum, id_Tags) VALUES(1, 'thirdDocument', 'path3', '1092941466', 1112)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO documents(id_User, name, path, datum, id_Tags) VALUES(2, 'fourthDocument', 'path4', '1092941466', 1211)"
cursor.execute(sql)
connection.commit()

# -- tags
sql = "INSERT INTO tags(id, name, id_Parent) VALUES(10, 'Chemie', 0)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES(11, 'Informatik', 0)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES(12, 'Deutsch', 0)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES(1010, 'gym1', 10)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES(1011, 'gym2', 10)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES(1012, 'gym3', 10)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES(1013, 'gym4', 10)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES(1110, 'gym1', 11)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES(1111, 'gym2', 11)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES(1210, 'gym1', 12)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES(1211, 'gym2', 12)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES(1212, 'gym3', 12)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES(1213, 'gym4', 12)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES(101010, 'Juchler', 1010)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES(101110, 'Juchler', 1011)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES(101210, 'Juchler', 1012)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES(101310, 'Juchler', 1013)"
cursor.execute(sql)
connection.commit()

# -- comments
sql = "INSERT INTO comments(id_Document, id_User, comment, datum) VALUES(1, 3, 'Ein völlig sinnloser Kommentar', '1092941466')"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO comments(id_Document, id_User, comment, datum) VALUES(2, 1, 'Ein völlig sinnvoller Kommentar', '1092941466')"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO comments(id_Document, id_User, comment, datum) VALUES(3, 2, 'Ein weiterer Kommentar', '1092941466')"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO comments(id_Document, id_User, id_Comment, comment, datum) VALUES(2, 3, 2, 'Ein rekursiver Kommentar', '1092941466')"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO likes(id_User, id_Document) VALUES(1, 1)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO likes(id_User, id_Document) VALUES(2, 1)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO likes(id_User, id_Document) VALUES(2, 2)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO likes(id_User, id_Comment) VALUES(3, 3)"
cursor.execute(sql)
connection.commit()

connection.close()

#Datum Unix Timestamp format
