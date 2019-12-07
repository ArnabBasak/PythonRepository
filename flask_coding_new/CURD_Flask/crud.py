import sqlite3
from flask import *


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/add")
def add():
    return render_template('add.html')

@app.route("/savedetails",methods = ["POST","GET"])
def saveDetails():
    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["contact"]
            address = request.form["address"]
            con = sqlite3.connect("employee.db")
            cur = con.cursor()
            con.execute("INSERT into employee (name, email, address) values (?,?,?)",(name,email,address))
            con.commit()
            msg = "employee successfully added"
            con.close()
            return render_template("success.html",msg=msg)
        except:
            msg = "failed to add employee"
            return render_template('success.html',msg=msg)

@app.route("/views")
def view():
    con = sqlite3.connect('employee.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute('select * from employee')
    rows = cur.fetchall()
    print(rows)
    return render_template('views.html',rows=rows)

@app.route("/delete")
def delete():
    return render_template("delete.html")

@app.route("/deleterecord",methods = ["POST"])
def deleterecord():
    id = request.form["id"]
    con = sqlite3.connect('employee.db')
    try:
        cur = con.cursor()
        con.execute("delete from employee where id = ?",id)
        con.commit()
        msg = "record successfully deleted"
        return render_template('delete_record.html',msg=msg)
    except:
        msg = "cannot delete"
        return render_template('delete_record.html',msg=msg)
if __name__ == "__main__":
    app.run(debug = True)
