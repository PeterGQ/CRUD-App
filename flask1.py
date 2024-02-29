import sqlite3

connection = sqlite3.connect("HW2.db")
cursor = connection.cursor()

command = """CREATE TABLE IF NOT EXISTS users(Name TEXT, Id TEXT, Points TEXT)"""

cursor.execute(command)
cursor.execute("INSERT INTO users VALUES ('Steve Smith','211','80')")
cursor.execute("INSERT INTO users VALUES ('Jian Wong','122','92')")
cursor.execute("INSERT INTO users VALUES ('Chris Peterson','213','91')")
connection.commit()

