import sqlite3


con = sqlite3.connect('GymBoard.db')
cur = con.cursor()

sql = "CREATE TABLE comments(" \
      "id INTEGER NOT NULL UNIQUE, " \
      "id_Comments INTEGER NOT NULL UNIQUE, " \
      "id_Documents INTEGER NOT NULL UNIQUE, " \
      "id_User INTEGER NOT NULL UNIQUE, " \
      "comment TEXT NOT NULL, " \
      "datum TEXT NOT NULL)"
cur.execute(sql)

sql = "CREATE TABLE document(" \
      "id INTEGER NOT NULL UNIQUE, " \
      "id_user INTEGER NOT NULL UNIQUE, " \
      "path TEXT NOT NULL UNIQUE, " \
      "datum TEXT NOT NULL)"
cur.execute(sql)

sql = "CREATE TABLE likes(" \
      "id INTEGER NOT NULL UNIQUE, " \
      "id_User INTEGER NOT NULL UNIQUE, " \
      "id_Document INTEGER NOT NULL UNIQUE, " \
      "id_Comment INTEGER UNIQUE)"
cur.execute(sql)

sql = "CREATE TABLE tags(" \
      "id INTEGER NOT NULL UNIQUE, " \
      "name TEXT NOT NULL UNIQUE, " \
      "level INTEGER)"
cur.execute(sql)

sql = "CREATE TABLE tags_Document(" \
      "id INTEGER NOT NULL UNIQUE, " \
      "id_Tags INTEGER NOT NULL UNIQUE, " \
      "id_Document INTEGER NOT NULL UNIQUE)"
cur.execute(sql)

sql = "CREATE TABLE user(" \
      "id INTEGER NOT NULL UNIQUE, " \
      "eMail TEXT NOT NULL UNIQUE, " \
      "nickName TEXT NOT NULL UNIQUE, " \
      "link TEXT UNIQUE, " \
      "lTime INTEGER, " \
      "status INTEGER NOT NULL, " \
      "role	INTEGER NOT NULL, " \
      "datum TEXT NOT NULL)"
cur.execute(sql)

con.close()
