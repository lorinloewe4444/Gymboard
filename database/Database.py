import sqlite3


con = sqlite3.connect('GymBoard.db')
cur = con.cursor()

sql = "CREATE TABLE comment(" \
      "id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT, " \
      "id_Comment INTEGER, " \
      "id_Document INTEGER NOT NULL, " \
      "id_User INTEGER NOT NULL, " \
      "comment TEXT NOT NULL, " \
      "datum TEXT NOT NULL)"
cur.execute(sql)

sql = "CREATE TABLE document(" \
      "id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT, " \
      "id_User INTEGER NOT NULL, " \
      "name TEXT NOT NULL, " \
      "path TEXT NOT NULL UNIQUE, " \
      "datum TEXT NOT NULL)"
cur.execute(sql)

sql = "CREATE TABLE like(" \
      "id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT, " \
      "id_User INTEGER NOT NULL, " \
      "id_Document INTEGER, " \
      "id_Comment INTEGER)"
cur.execute(sql)

sql = "CREATE TABLE tag(" \
      "id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT, " \
      "name TEXT NOT NULL UNIQUE, " \
      "level INTEGER)"
cur.execute(sql)

sql = "CREATE TABLE tag_Document(" \
      "id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT, " \
      "id_Tag INTEGER NOT NULL, " \
      "id_Document INTEGER NOT NULL)"
cur.execute(sql)

sql = "CREATE TABLE user(" \
      "id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT, " \
      "eMail TEXT NOT NULL UNIQUE, " \
      "nickName TEXT NOT NULL UNIQUE, " \
      "link TEXT, " \
      "lTime INTEGER, " \
      "status INTEGER NOT NULL, " \
      "role	INTEGER NOT NULL, " \
      "datum TEXT NOT NULL)"
cur.execute(sql)

con.close()
