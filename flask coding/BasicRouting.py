from flask import Flask
app = Flask(__name__)
#@ signifies a decorator - way to wrap a function and modifying its behaviour
@app.route('/')
def index():
    return 'welcome to my home page of python'

@app.route('/arnab')
def arnab():
    return'<h2> Arnab home page</h2>'

@app.route('/profile/<username>')
def profile(username):
    return "<h2>hello %s </h2>" % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return "<h2>Post iD is  %s </h2>" % post_id


if __name__== '__main__':
    app.run()
