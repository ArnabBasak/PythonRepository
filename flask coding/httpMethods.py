# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 21:18:14 2018

@author: Arnab
"""

from flask import Flask,request
app = Flask(__name__)
@app.route("/")
def index():
    return "method used: %s" %request.method
@app.route("/mypage",methods=['GET','POST'])
def mypage():
    if request.method == 'POST':
        return "you are using post method"
    else:
        return "you are using get method"
if __name__ == "__main__":
    app.run()