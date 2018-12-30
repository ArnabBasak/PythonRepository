#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 23:12:47 2018

@author: arnabbasak
"""

# A simple function to calculate the value 3x+1
#anonymous function == lambda expression

#lambda just like function its perfectly acceptable to have a function without any name
#cannot use lambda expression for multiline values

def f(x):
    return 3*x+1
print(f(2))

g = lambda x: 3*x+1
print(g(2))

#lambda expression with more than one input 
#combine first and last name into a single name

full_name = lambda fn,ln:fn.strip().title() + " " + ln.strip().title()
print(full_name("   Arnab","BASAK"))

scifi_authors = ["Issac Asimov", "Ray Braduary", "Robert Heinlein"," Arthur .c. Clark","Frank Herbert","Orsan scott card","Douglas Adams","H. G. Wells","Leigh Brackett"]
#sort this list in alphabetic order through anonimous function
#sorting the list on the last name
scifi_authors.sort(key=lambda name:name.split(" ")[-1].lower())
print(scifi_authors)

def build_quadratic_equations(a,b,c):
    return lambda x: a*x**2 + b*x + c
#f = build_quadratic_equations(2,3,-5)
#print(f(2))
print(build_quadratic_equations(3,0,1)(2)) # evaluate 3x^2+1

#common application for lambda expression is sorting and flitering data
