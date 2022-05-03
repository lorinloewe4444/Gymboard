import sqlite3


con = sqlite3.connect('GymBoard.db')
cur = con.cursor()

sql = "CREATE TABLE comments(" \
      "id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT, " \
      "id_Comment INTEGER, " \
      "id_Document INTEGER NOT NULL, " \
      "id_User INTEGER NOT NULL, " \
      "comment TEXT NOT NULL, " \
      "datum INTEGER NOT NULL)"
cur.execute(sql)

sql = "CREATE TABLE documents(" \
      "id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT, " \
      "id_User INTEGER NOT NULL, " \
      "name TEXT NOT NULL, " \
      "path TEXT NOT NULL UNIQUE, " \
      "datum INTEGER NOT NULL)"
cur.execute(sql)

sql = "CREATE TABLE likes(" \
      "id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT, " \
      "id_User INTEGER NOT NULL, " \
      "id_Document INTEGER, " \
      "id_Comment INTEGER)"
cur.execute(sql)

sql = "CREATE TABLE tags(" \
      "id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT, " \
      "name TEXT NOT NULL UNIQUE, " \
      "level INTEGER)"
cur.execute(sql)

sql = "CREATE TABLE tags_Documents(" \
      "id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT, " \
      "id_Tag INTEGER NOT NULL, " \
      "id_Document INTEGER NOT NULL)"
cur.execute(sql)

sql = "CREATE TABLE users(" \
      "id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT, " \
      "eMail TEXT NOT NULL UNIQUE, " \
      "nickName TEXT NOT NULL UNIQUE, " \
      "link TEXT, " \
      "lTime INTEGER, " \
      "status INTEGER NOT NULL, " \
      "role	INTEGER NOT NULL, " \
      "datum INTEGER NOT NULL)"  #Unix Timestamp        datetime(time-value, 'unixepoch')
cur.execute(sql)

con.close()
