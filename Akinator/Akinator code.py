# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas
print('CRICKET AKINATOR THINK OF ANY CRICKETER AND I WILL GUESS IT\n PLEASE GIVE YES OR NO AS THE ANSWERS')
Userinput = input('IS YOUR CRICKETER A BATSMAN')
if Userinput == 'y':
    print('your circketer is sachin tendulkar')
elif Userinput == 'n':
    Userinput = input('IS YOUR CRICKTER A BOWLER')
    if Userinput == 'y':
        bowlerdataframe = pandas.read_csv('E:/pythonprograms/Akinator/bowlerrecords.csv')
        print(bowlerdataframe)
    else:
        print('PLEASE SELECT FOR A BOWLER OR A BATSMAN')
else:
    print('INVALID INPUT PLEASE SELECT A PROPER ONE THAT IS ''y OR n''')
