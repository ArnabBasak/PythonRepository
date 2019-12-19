from flask import *

app = Flask(__name__)
@app.route("/calculation",methods=["POST","GET"])
def addition():
    msg = ""
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        #city = request.form["city"]
        #password = request.form["password"]
        #username = request.form["username"]
        #reenterpassword = request.form["reenterpassword"]
        return render_template('addition.html')
    else:
        return render_template('addition.html')
if __name__ == '__main__':
    app.run(debug=True)
