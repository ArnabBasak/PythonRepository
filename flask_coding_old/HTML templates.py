# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 21:35:28 2018

@author: Arnab
"""

from flask import Flask,render_template
app = Flask(__name__)
#@app.route("/profile/<name>")
#def profile(name):
#    return render_template("profile.html",name=name)
@app.route("/")
@app.route("/<user>")
def index(user= None):
    return render_template("user.html",user = user)

@app.route("/shopping")
def shopping():
    food = ["cheese","cake","ice creame"]
    return render_template("shopping.html",food=food)

if __name__ == "__main__":
    app.run()