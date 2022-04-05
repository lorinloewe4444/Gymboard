import sqlite3

connection = sqlite3.connect('GymBoard.db')
cursor = connection.cursor()

# -- user
sql = "INSERT INTO users(eMail, nickName, status, role, datum) VALUES('asterix.gallien@stud.gyminterlaken.ch', 'asterix', 0, 0, '22:03:29')"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO users(eMail, nickName, status, role, datum) VALUES('idefix.gallien@stud.gyminterlaken.ch', 'idefix', 1, 1, '22:03:29')"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO users(eMail, nickName, status, role, datum) VALUES('obelix.gallien@stud.gyminterlaken.ch', 'obelix', 1, 1, '22:03:29')"
cursor.execute(sql)
connection.commit()

# -- document
sql = "INSERT INTO documents(id_User, name, path, datum) VALUES(1, 'firstDocument', 'path1', '22:03:30')"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO documents(id_User, name, path, datum) VALUES(3, 'secondDocument', 'path2', '22:03:30')"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO documents(id_User, name, path, datum) VALUES(1, 'thirdDocument', 'path3', '22:03:30')"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO documents(id_User, name, path, datum) VALUES(2, 'fourthDocument', 'path4', '22:03:30')"
cursor.execute(sql)
connection.commit()

# -- tags
sql = "INSERT INTO tags(name, level) VALUES('gym1', 0)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(name, level) VALUES('gym2', 0)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(name, level) VALUES('Chemie', 1)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(name, level) VALUES('Juchler', 2)"
cursor.execute(sql)
connection.commit()

# -- tags_Document
sql = "INSERT INTO tags_Documents(id_Document, id_Tag) VALUES(1, 1)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags_Documents(id_Document, id_Tag) VALUES(1, 3)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags_Documents(id_Document, id_Tag) VALUES(1, 4)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags_Documents(id_Document, id_Tag) VALUES(2, 2)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags_Documents(id_Document, id_Tag) VALUES(3, 2)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags_Documents(id_Document, id_Tag) VALUES(4, 1)"
cursor.execute(sql)
connection.commit()

# -- comments
sql = "INSERT INTO comments(id_Document, id_User, comment, datum) VALUES(1, 3, 'Ein völlig sinnloser Kommentar', '22:03:29')"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO comments(id_Document, id_User, comment, datum) VALUES(2, 1, 'Ein völlig sinnvoller Kommentar', '22:03:29')"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO comments(id_Document, id_User, comment, datum) VALUES(3, 2, 'Ein weiterer Kommentar', '22:03:29')"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO comments(id_Document, id_User, id_Comment, comment, datum) VALUES(2, 3, 2, 'Ein rekursiver Kommentar', '22:03:29')"
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

sql = "INSERT INTO likes(id_User, id_Document, id_Comment) VALUES(3, 3, 3)"
cursor.execute(sql)
connection.commit()

connection.close()
