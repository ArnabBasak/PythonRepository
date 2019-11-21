from flask import Flask

app = Flask(__name__) #creating the flask object
@app.route('/')
def home():
    return "hello this is first flask website"


if __name__ == '__main__':
    app.run(debug=True)
