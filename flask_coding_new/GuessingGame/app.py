from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    username = request.args.get('username')
    password = request.args.get('password')
    if username == "admin" and password == "admin":
        return render_template('home.html')
    else:
        return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    if username == "admin" and password == "admin":
        return render_template('login.html')
    else:
        return render_template('register.html')
if __name__ == "__main__":
        app.run(debug=True)
