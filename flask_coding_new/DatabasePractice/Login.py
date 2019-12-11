import sqlite3
from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login")
def index():
    return render_template('login.html')

@app.route("/register")
def index():
    return render_template('registration.html')

if __name__ == '__main__':
    app.run(debug=True)
