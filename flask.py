from flask import Flask, render_template,request,json
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',user='user',password='passwd',db='db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
app = Flask(__name__)

@app.route("/get-reg")
def login():
    return render_template('reg.html')

@app.route('/save-post',methods=['POST', 'GET'])
def signUp():
    if request.method=='POST':
     name=request.form['name']
     email=request.form['email']
     try:
  

      with connection.cursor() as cursor:
      # Read a single record
        sql = "INSERT INTO userdata (username,email) VALUES (%s, %s)"
        cursor.execute(sql, (name,email))
        connection.commit()
     finally:
      connection.close()
      return "Saved successfully."
    else:
      return "error"