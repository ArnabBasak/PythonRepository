from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "hello this is my site"

@app.route('/home/<name>')
def name(name):
    return "hello"+name

@app.route('/home/<int:age>')
def age(age):
    return "Age = %d"%age;

if __name__ == '__main__':
    app.run(host='localhost',port=5000,debug=True)
