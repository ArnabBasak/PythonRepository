from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'welcome to my home page of python'
if __name__== '__main__':
    app.run()
