import sqlite3

with sqlite3.connect("PhoneBook2.db") as db:
    cursor=db.cursor()
cursor.execute(""" CREATE TABLE IF NOT EXISTS Names(
id integer PRIMARY KEY,
firstname text,
surname text,
phonenumber text); """)

cursor.execute(""" INSERT INTO NAMES (id, firstname, surname, phonenumber)
VALUES("1", "Jonghwa", "Lee", "000 000 0000")""")
db.commit()

cursor.execute(""" INSERT INTO NAMES(id, firstname, surname, phonenumber)
VALUES("2", "JJ", "Lee", "111 111 1111")""")
db.commit()

cursor.execute(""" INSERT INTO NAMES(id, firstname, surname, phonenumber)
VALUES("3", "HH", "Lee", "222 222 2222")""")
db.commit()

cursor.execute(""" INSERT INTO NAMES(id, firstname, surname, phonenumber)
VALUES("4", "JH", "Lee", "333 333 3333")""")
db.commit()

cursor.execute(""" INSERT INTO NAMES(id, firstname, surname, phonenumber)
VALUES("5", "JJHH", "Lee", "444 444 4444")""")
db.commit()

db.close()