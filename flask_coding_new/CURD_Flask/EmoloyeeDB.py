import sqlite3
con = sqlite3.connect("employee.db")
print('successfully connected')
con.execute("""create table employee(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
email TEXT UNIQUE NOT NULL,
address TEXT NOT NULL)""")
print("table created successfully")
con.close()
