from flask import *
import pymysql

app = Flask('app')

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host="localhost",port=5000,debug=True)
