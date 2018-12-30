#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 18:12:59 2018

@author: arnabbasak
"""

mytxtfile = open('modi_speech.txt','r')
example_sent = mytxtfile.read().replace('\n','')
print(len(example_sent))
uppercasecount = 0
lowercasecount = 0
for element in example_sent:
    if(element.islower()):
        uppercasecount = uppercasecount+1
    elif(element.isupper()):
        lowercasecount = lowercasecount+1
print('upper case count in the file is',uppercasecount)
print('lower case count in the file is',lowercasecount)
print('precentage of the upper case letter in the file')
print(((uppercasecount)/(len(example_sent)))*100)
print('precentage of the lower case letter in the file')
print(((lowercasecount)/(len(example_sent)))*100)



