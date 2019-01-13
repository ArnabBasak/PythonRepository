# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
print('**********WELCOME TO PYTHON CALCULATOR**********')
print('---ENTER YOUR OPRION---')
option = int(input('---1.NORMAL CALCULATOR---\n---2.SCIENTIFIC CALCULATOR---\n'))
if option == 1:
    print('....THIS IS SIMPLE CALCULATOR....')        
    operator = input('a.ADDITION\ns.SUBSTRACTION\nm.MULTIPLY\nd.DIVISION\nx.EXIT\n')
    if operator == 'a':
        num = int(input('How many number do you want to addn\n'))
        print('enter the numbers\n')
        addlist = []
        while len(addlist) < num:
            numbers = int(input())  
            addlist.append(numbers)
        print('Addition of all the numbers is',sum(addlist))
    elif operator == 's':
        print('Sorry its under development you can enter only two numbers for substraction\n')
        number1 = int(input('enter number 1\n'))
        number2 = int(input('enter number 2\n'))
        print('Substraction is',number1 - number2)
    elif operator == 'm':
        num = int(input('How many number do you want to multiply\n'))
        print('enter the numbers\n')
        mullist = []
        while len(mullist) < num:
            numbers = int(input())  
            mullist.append(numbers)
            result = np.prod(np.array(mullist))
        print('multiplication of all the numbers is',result)
    elif operator == 'd':
        print('enter two numbers for division\n')
        number1 = int(input('enter first number'))
        number2 = int(input('enter second number'))
        try:
            result = number1/number2
        except:
            print('Second number is 0 so it cannot divide')
    elif operator == 'x':
            print('THANK YOU')
elif option == 2:
        print('....THIS IS SCIENTIFIC CALCULATOR....')
        part = int(input('Enter 1 for binary calculator\n Enter 2 for normal scientific calculation'))
        if part == 1:
            dec = int(input('enter a decimal number to convert'))
            choice = input('enter b for binary\n o for octal \n h for hexadecimal\n')
            if choice == 'b':
                print("binary of the entered number is: ",bin(dec))
            elif choice == 'o':
                print("octal of the entered number is: ",oct(dec))
            elif choice == 'h':
                print("hexadecimal of the entered number is: ",hex(dec))
            else:
                print('Not proper input for binary conversion')
        elif part == 2:
            print('thanks for choosing that option, but sorry to say that its currently under development')
        else:
            print('please select the option properly')
else:
        print('select proper option')

