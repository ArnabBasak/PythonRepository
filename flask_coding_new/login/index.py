from flask import *
import pymysql

app = Flask(__name__)
@app.route("/",methods=["POST","GET"])
def index():
    msg = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if (len(username) and len(password) == 0):
            msg = "please fill the details properly"
            return render_template('/',msg = msg)
        else:
            db = pymysql.connect("localhost","root","library","user")
            cursor = db.cursor()
            sql = """select username,password from login where username like ('%s') and password like ('%s')""" %(username,password)
            output = cursor.execute(sql)
            print(output)
            if output == 2:
                return render_template('home.html')
            else:
                msg = "invalid credentials"
                return render_template('index.html',msg = msg)


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
        if (len(name) or len(city) or len(username) or len(email) or len(city) or len(password) or len(reenterpassword)) == 0:
            msg = "please fill the details properly"
            return render_template('register.html',msg = msg)
        elif password.lower() != reenterpassword.lower():
            msg = "please check the reconfirm password"
            return render_template('register.html',msg = msg)
        else:
            db = pymysql.connect("localhost","root","library","user")
            cursor = db.cursor()
            sql = """select username from login where username like ('%s')""" %(username)
            username_check = cursor.execute(sql)
            if username_check == 0:
                sql = """insert into login(username,password) values ('%s','%s')""" %(username,password)
                cursor.execute(sql)
                db.commit()
                msg = "Customer details saved successfully"
                return render_template("register.html",msg=msg)
            else:
                msg = "username already exists"
                return render_template("register.html",msg=msg)
            sql = """insert into user(name,email,address) values ('%s','%s','%s')""" %(name,email,city)
            cursor.execute(sql)
            db.commit()
    else:
        return render_template('register.html')

@app.route("/home",methods=["GET","POST"])
def home():
    msg = ""
    if request.method == "POST":
        first_num = request.form["first_num"]
        second_num = request.form["second_num"]
        option = request.form["operation"]
        if len(first_num) and len(second_num) == 0:
            msg = "please fill all the feilds properly"
            return render_template("home.html",msg = msg)
        else:
            if option == "addition":
                msg = "Addition is " + str(int(first_num) + int(second_num))
                return render_template("home.html",msg = msg)
            elif option == "substraction":
                msg = "substraction is " + str(int(first_num) - int(second_num))
                return render_template("home.html",msg = msg)
            elif option == "division":
                if second_num == 0:
                    msg = "sorry cannot divide "
                    return render_template("home.html",msg = msg)
                else:
                    msg = "DIvision is " + str(int(first_num) / int(second_num))
                    return render_template("home.html",msg = msg)
            elif option == "multiplication":
                msg = msg = "multiplication is " + str(int(first_num) * int(second_num))
                return render_template("home.html",msg = msg)
            else:
                msg = "Please select the option properly"
                return render_template("home.html",msg = msg)
@app.route("/simpleinterest",methods=["GET","POST"])
def simpleinterest():
    if method == request.method == "POST":
        amount = request.form["principle"]
        roi = request.form["roi"]
        period = request.form["period"]
        #if len(amount)
if __name__ == '__main__':
    app.run(debug=True)



    #PosSetUp@321
