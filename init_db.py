import os
import sqlite3

if not os.path.exists('data'):
    os.makedirs('data')
connection = sqlite3.connect("data/database.db")

with open("schema.sql") as f:
    connection.executescript(f.read())

connection.commit()
connection.close()