from flask import *
import pymysql

app = Flask('app')

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="localhost",port=5000,debug=True)
