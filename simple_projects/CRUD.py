import sqlite3
class databaseOperation:
    def __init__(self):
        self.query = ''
        self.conn = sqlite3.connect('Student.db')
    def createtable(self):
        self.query = """
        CREATE TABLE IF NOT EXISTS student (
        ID int PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        AGE INT NOT NULL,
        ADDRESS CHAR(50));"""
        self.conn.execute(self.query)
        print('Table created successfully')
    def insertdata(self):
        self.query = f"INSERT INTO student(ID,name,age,address) values({self.id},'{self.name}',{self.age},'{self.address}')"
        print(self.query)
        self.conn.execute(self.query)
        self.conn.commit()
    def getdata(self):
        self.id = int(input('enter ID'))
        self.name = input('Enter your name')
        self.age = int(input('Enter the age'))
        self.address = input('Enter the address')
        self.insertdata()
    def readdata(self):
        self.query = "select * from student"
        self.data = self.conn.execute(self.query)
        for items in self.data:
            print(f"ID = {items[0]}")
            print(f"NAME = {items[1]}")
            print(f"AGE = {items[2]}")
            print(f"ADDRESS = {items[3]}")
db = databaseOperation()
db.createtable()
db.getdata()
db.readdata()
