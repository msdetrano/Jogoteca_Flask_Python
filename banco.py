import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully")

conn.execute('CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, categoria TEXT, console TEXT)')
print("Table created successfully")

conn.close()