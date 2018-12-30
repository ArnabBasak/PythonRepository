#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 23:08:56 2018

@author: arnabbasak
"""

def fib():
    a,b = 0,1
    while True:
        yield  a
        a,b = b,a+b
for f in fib():
    if f > 13:
        break
    print (f)