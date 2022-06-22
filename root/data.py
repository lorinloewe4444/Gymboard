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

#------------------------------------------------------------------------
# BG 11xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (1110, 'Grundlagenfach', 11)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (1111, 'Schwerpunktfach', 11)"
cursor.execute(sql)
connection.commit()

# BG - Grundlagenfach - 1110xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (111010, 'Gym 1', 1110)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (111011, 'Gym 2', 1110)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (111012, 'Gym 3', 1110)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (111013, 'Gym 4', 1110)"
cursor.execute(sql)
connection.commit()

# BG - Schwerpunktfach - 1111xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (111110, 'Gym 1', 1111)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (111111, 'Gym 2', 1111)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (111112, 'Gym 3', 1111)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (111113, 'Gym 4', 1111)"
cursor.execute(sql)
connection.commit()

#------------------------------------------------------------------------------
# Chemie 12xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (1210, 'Grundlagenfach', 12)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (1211, 'Schwerpunktfach', 12)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (1212, 'Ergänzungsfach', 12)"
cursor.execute(sql)
connection.commit()

# Chemie - Grundlagenfach - 1210xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (121010, 'Einsprachig', 1210)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (121011, 'Zweisprachig', 1210)"
cursor.execute(sql)
connection.commit()

# Chemie - Grundlagenfach - Einsprachig - 121010xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (12101010, 'Gym 1', 121010)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (12101011, 'Gym 2', 121010)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (12101012, 'Gym 3', 121010)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (12101013, 'Gym 4', 121010)"
cursor.execute(sql)
connection.commit()

# Chemie - Grundlagenfach - Zweisprachig - 121011
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (12101110, 'Gym 1', 121011)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (12101111, 'Gym 2', 121011)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (12101112, 'Gym 3', 121011)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (12101113, 'Gym 4', 121011)"
cursor.execute(sql)
connection.commit()

# Chemie - Schwerpunktfach - 1211xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (121110, 'Gym 1', 1211)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (121111, 'Gym 2', 1211)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (121112, 'Gym 3', 1211)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (121113, 'Gym 4', 1211)"
cursor.execute(sql)
connection.commit()

# Chemie - Ergänzungsfach - 1212xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (121210, 'Gym 1', 1212)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (121211, 'Gym 2', 1212)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (121212, 'Gym 3', 1212)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (121213, 'Gym 4', 1212)"
cursor.execute(sql)
connection.commit()

#------------------------------------------------------------------------
# Deutsch 14xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (1410, 'Gym 1', 14)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (1411, 'Gym 2', 14)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (1412, 'Gym 3', 14)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (1413, 'Gym 4', 14)"
cursor.execute(sql)
connection.commit()

#-------------------------------------------------------------------------------
# Englisch 15xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (1510, 'Grundlagenfach', 15)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (1511, 'Schwerpunktfach', 15)"
cursor.execute(sql)
connection.commit()

# Englisch - Grundlagenfach - 1510xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (151010, 'Gym 1', 1510)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (151011, 'Gym 2', 1510)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (151012, 'Gym 3', 1510)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (151013, 'Gym 4', 1510)"
cursor.execute(sql)
connection.commit()

# Englisch - Schwerpunktfach - 1511xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (151110, 'Gym 1', 1511)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (151111, 'Gym 2', 1511)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (151112, 'Gym 3', 1511)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (151113, 'Gym 4', 1511)"
cursor.execute(sql)
connection.commit()

#-------------------------------------------------------------------------------
# WR 16xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (1610, 'EWR', 16)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (1611, 'Schwerpunktfach', 16)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (1612, 'Ergänzungsfach', 16)"
cursor.execute(sql)
connection.commit()

# WR - Schwerpunktfach - 1611xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (161110, 'Gym 1', 1611)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (161111, 'Gym 2', 1611)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (161112, 'Gym 3', 1611)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (161113, 'Gym 4', 1611)"
cursor.execute(sql)
connection.commit()

# WR - Ergänzungsfach - 1612xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (161210, 'Gym 3', 1612)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (161211, 'Gym 4', 1612)"
cursor.execute(sql)
connection.commit()

#-------------------------------------------------------------------------------
# Französisch 17xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (1710, 'Gym 1', 17)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (1711, 'Gym 2', 17)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (1712, 'Gym 3', 17)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (1713, 'Gym 4', 17)"
cursor.execute(sql)
connection.commit()

#-------------------------------------------------------------------------------
# Geschichte 18xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (1810, 'Einsprachig', 18)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (1811, 'Zweisprachig', 18)"
cursor.execute(sql)
connection.commit()

# Geschichte - Einsprachig - 1810xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (181010, 'Gym 1', 1810)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (181011, 'Gym 2', 1810)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (181012, 'Gym 3', 1810)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (181013, 'Gym 4', 1810)"
cursor.execute(sql)
connection.commit()

# Geschichte - Zweisprachig - 1811xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (181110, 'Gym 1', 1811)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (181111, 'Gym 2', 1811)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (181112, 'Gym 3', 1811)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (181113, 'Gym 4', 1811)"
cursor.execute(sql)
connection.commit()

#-----------------------------------------------------------------------------
# Geografie 19xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (1910, 'Grundlagenfach', 19)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (1911, 'Ergänzungsfach', 19)"
cursor.execute(sql)
connection.commit()

# Geografie - Grundlagenfach - 1910xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (191010, 'Gym 1', 1910)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (191011, 'Gym 2', 1910)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (191012, 'Gym 4', 1910)"
cursor.execute(sql)
connection.commit()

# Geografie - Ergänzungsfach - 1911xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (191110, 'Gym 3', 1911)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (191111, 'Gym 4', 1911)"
cursor.execute(sql)
connection.commit()

#------------------------------------------------------------------------------
# Italienisch 21xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (2110, 'Schwerpunktfach', 21)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (2111, 'Fakultativfach', 21)"
cursor.execute(sql)
connection.commit()

# Italienisch - Schwerpunktfach - 1210xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (211010, 'Gym 1', 2110)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (211011, 'Gym 2', 2110)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (211012, 'Gym 3', 2110)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (211013, 'Gym 4', 2110)"
cursor.execute(sql)
connection.commit()

# Italienisch - Fakultativfach - 2111xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (211110, 'Gym 1', 2111)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (211111, 'Gym 2', 2111)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (211112, 'Gym 3', 2111)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (211113, 'Gym 4', 2111)"
cursor.execute(sql)
connection.commit()

#-------------------------------------------------------------------------------
# Informatik 22xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (2210, 'Grundlagenfach', 22)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (2211, 'Ergänzungsfach', 22)"
cursor.execute(sql)
connection.commit()

# Informatik - Grundlagenfach - 2210xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (221010, 'Gym 1', 2210)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (221011, 'Gym 2', 2210)"
cursor.execute(sql)
connection.commit()

# Informatik - Ergänzungsfach - 2211xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (221110, 'Gym 3', 2211)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (221111, 'Gym 4', 2211)"
cursor.execute(sql)
connection.commit()

#------------------------------------------------------------------------------
# Latein 23xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (2310, 'Schwerpunktfach', 23)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (2311, 'Fakultativfach', 23)"
cursor.execute(sql)
connection.commit()

# Latein - Schwerpunktfach - 2310xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (231010, 'Gym 1', 2310)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (231011, 'Gym 2', 2310)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (231012, 'Gym 3', 2310)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (231013, 'Gym 4', 2310)"
cursor.execute(sql)
connection.commit()

# Latein - Fakultativfach - 2311xx

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (231110, 'Gym 1', 2311)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (231111, 'Gym 2', 2311)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (231112, 'Gym 3', 2311)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (231113, 'Gym 4', 2311)"
cursor.execute(sql)
connection.commit()

#-------------------------------------------------------------------------------
# Mathematik 24xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (2410, 'Gym 1', 24)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (2411, 'Gym 2', 24)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (2412, 'Gym 3', 24)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (2413, 'Gym 4', 24)"
cursor.execute(sql)
connection.commit()

#---------------------------------------------------------------------------------
# Musik 25xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (2510, 'Grundlagenfach', 25)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (2511, 'Ergänzungsfach', 25)"
cursor.execute(sql)
connection.commit()

# Musik - Grundlagenfach - 2510xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (251010, 'Gym 1', 2510)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (251011, 'Gym 2', 2510)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (251012, 'Gym 3', 2510)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (251013, 'Gym 4', 2510)"
cursor.execute(sql)
connection.commit()

# Musik - Ergänzungsfach - 2511xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (251110, 'Gym 1', 2511)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (251111, 'Gym 2', 2511)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (251112, 'Gym 3', 2511)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (251113, 'Gym 4', 2511)"
cursor.execute(sql)
connection.commit()

#------------------------------------------------------------------------------
# Physik 26xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (2610, 'Gym 2', 26)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (2611, 'Gym 3', 26)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (2612, 'Gym 4', 26)"
cursor.execute(sql)
connection.commit()

#------------------------------------------------------------------------------
# PAM 27xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (2710, 'Mathematik', 27)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (2711, 'Physik', 27)"
cursor.execute(sql)
connection.commit()

# PAM - Mathematik - 2710xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (271010, 'Gym 1', 2710)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (271011, 'Gym 2', 2710)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (271012, 'Gym 3', 2710)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (271013, 'Gym 4', 2710)"
cursor.execute(sql)
connection.commit()

# PAM - Physik - 2711xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (271110, 'Gym 1', 2711)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (271111, 'Gym 2', 2711)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (271112, 'Gym 3', 2711)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (271113, 'Gym 4', 2711)"
cursor.execute(sql)
connection.commit()

#-------------------------------------------------------------
# PPP 28xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (2810, 'Philosophie', 28)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (2811, 'Psychologie', 28)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (2812, 'Pädagogik', 28)"
cursor.execute(sql)
connection.commit()

# PPP - Philosophie - 2810xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (281010, 'Gym 1', 2810)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (281011, 'Gym 2', 2810)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (281012, 'Gym 3', 2810)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (281013, 'Gym 4', 2810)"
cursor.execute(sql)
connection.commit()

# PPP - Psychologie - 2811xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (281110, 'Gym 1', 2811)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (281111, 'Gym 2', 2811)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (281112, 'Gym 3', 2811)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (281113, 'Gym 4', 2811)"
cursor.execute(sql)
connection.commit()

# PPP - Pädagogik - 2812xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (281210, 'Gym 1', 2812)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (281211, 'Gym 2', 2812)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (281212, 'Gym 3', 2812)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (281213, 'Gym 4', 2812)"
cursor.execute(sql)
connection.commit()

#-------------------------------------------------------------------------
# Sport 31xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (3110, 'Ergänzungsfach', 31)"
cursor.execute(sql)
connection.commit()

# Sport - Ergänzungsfach - 3110xx
sql = "INSERT INTO tags(id, name, id_Parent) VALUES (311010, 'Gym 3', 3110)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO tags(id, name, id_Parent) VALUES (311011, 'Gym 4', 3110)"
cursor.execute(sql)
connection.commit()

connection.close()
