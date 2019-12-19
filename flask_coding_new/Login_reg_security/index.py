from flask import *
import pymysql

app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/register",methods=["POST","GET"])
def register():
    msg = ""
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        city = request.form["city"]
        password = request.form["password"]
        username = request.form["username"]
        reenterpassword = request.form["reenterpassword"]
        if (len(name) and len(city) and len(username) and len(email) and len(city) and len(password) and len(reenterpassword)) == 0:
            msg = "please fill the details properly"
            return render_template('register.html',msg = msg)
        elif password.lower() != reenterpassword.lower():
            msg = "please check the reconfirm password"
            return render_template('register.html',msg = msg)
        else:
            db = pymysql.connect("localhost","root","library","user")
            cursor = db.cursor()
            sql = """insert into user(name,email,address) values ('%s','%s','%s')""" %(name,email,city)
            cursor.execute(sql)
            db.commit()
            sql = """insert into login(username,password) values ('%s','%s')""" %(username,password)
            cursor.execute(sql)
            db.commit()
            msg = "Customer details saved successfully"
            return render_template("register.html",msg=msg)
    else:
        return render_template('register.html')
if __name__ == '__main__':
    app.run(debug=True)
