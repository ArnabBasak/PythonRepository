import sqlite3
con = sqlite3.connect("student.db")
print("successfully connected")
con.execute("""create table if not exists student(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
password TEXT NOT NULL,
email TEXT UNIQUE NOT NULL,
address TEXT NOT NULL)""")
print('student table created')
con.close()
