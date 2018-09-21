import pymysql
conn =  pymysql.connect(host = "localhost",user = "root",password = "baban123",db = "world")
cur = conn.cursor()
cur.execute("select * from city")
#print(cur.description)
print()
for row in cur:
    print(row)

cur.close()
conn.close()
