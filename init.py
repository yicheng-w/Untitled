import sqlite3
from database import addSentence

"""THIS FILE IS USED TO CREATE THE BACKEND OF THE PROJECT, IT CREATES THE
DATABASE FILE AND CREATES ITS TABLES. ALL FUNCTIONS REGARDING CHANGING THE
DATABASE IS LOCATED AT database.py"""

conn = sqlite3.connect("infos.db")

c = conn.cursor()

q = "CREATE TABLE %s (%s)" # format string for creating tables,
                           # first formatter = name
                           # second formatter = arguments

c.execute(q % ("users", "username TEXT, password TEXT")) # NOTE: hex string will do fine for hash

c.execute(q % ("stories", "id TEXT, sentence TEXT, author TEXT, time INTEGER"))

c.execute(q % ("favorites", "id TEXT, username TEXT"))

addSentence(0,"HI! This is a sentence!","yeech")
addSentence(0,"HI! This is the second sentence in the first story","yeech")

conn.commit()
