import mysql.connector
db = mysql.connector.connect("localhost","root","password","test")
cursor =db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print(data)
