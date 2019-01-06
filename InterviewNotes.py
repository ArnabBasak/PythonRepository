#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""printing hello world"""
print('hello world')


# In[9]:


"""basic arithmatic"""
a,b = 9,2
print("addition is ",a+b)
print("substraction is ",a-b)
print("division is ",a/b)
print("Floor division ",a//b) """Floor division"""
print("modulus is ",a%b)
print("multiplication is ",a*b)
print("square is ",a**b)


# In[5]:


"""Taking user input"""
user_input = input('enter your name')
print('hello',user_input)


# In[13]:


"""even odd"""
a = 2
if a % 2 == 0:
    print(a,'is even')
else:
    print(b,'is odd')


# In[12]:


"""Positive negative zero"""
a = 3
if a > 0:
    print(a,"is positive number")
elif a < 0:
    print(a,"is negative number")
elif a == 0:
    print(a,'is zero')
else:
    print('enter a number')


# In[18]:


"""area of rectangel"""
l,b = 23,34
print('area of rectange',l*b)
"""area of circle"""
r= 23
print('area of circle',3.14*r*r)
"""are of square"""
s = 34
print('area of square',s*s)
"""area of triangle"""
a,b,c = 33,34,44
print('area of triangle',((a+b+c)/2))


# In[19]:


"""largest of three numbers"""
a,b,c = 564746,564434,567543
if a > b and a > c:
    print(a,'is greater')
elif b > a and b > c:
    print(b,'is greater')
elif c > a and c > b:
    print(c,' is greater')
else:
    print('all numbers are equal')


# In[22]:


"""palindrom of a string"""
mystring = 'aIbohPhoBiA'
clearstring = mystring.casefold()#ignores the case upper and lower 
rev_String = reversed(clearstring)
if list(rev_String) == list(clearstring):
    print('entered string is palindrome')
else:
    print('entered string is not palindrome')


# In[26]:


"""prime numbers"""
num = 407
if num > 1:
    for i in range(2,num):
        if(num % i) == 0:
            print(num,'is not prime')
            print(i,"times",num //i,'=is',num)
            break
    else:
        print(num,"is prime")


# In[36]:


"""factorial of a number"""
num = 7
factorial = 1
if num == 0:
    print('there is no factorial for 0')
elif num < 0:
    print('thre is no factorial for negative numbers')
else:
    for i in range(1,num+1):
        factorial = factorial *i
    print("the factorial of ",num,"is",factorial)


# In[38]:


"""multiplication table"""
num = 12
for i in range(1,11):
    print(num,"x",i,num*i)


# In[41]:


"""sum of natural numbers"""
num = 16
if num < 0:
    print('enter a positive number')
else:
    sum = 0
    while (num > 0):
        sum += num
        print(sum)
        num -= 1
        print(num)
    print('sum is ',sum)


# In[42]:


import math
num = 2
print("the square root of ",math.sqrt(num))


# In[43]:


"swapping of two variables with temporary variables and in single line"
a,b = 1,2
print('before swaping',a,b)
a,b = b,a
print('after swapping',a,b)


# In[44]:


"""Decimal to binary octal and hexadecimal conversion"""
num = 455
print('binary of ',num,bin(num))
print('octal of ',num,oct(num))
print('hexadecimal of ',num,hex(num))


# In[6]:


"""decorators"""
import time
def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__+"took"+str((end-start)*1000) + "mil second")
        return result
    return wrapper
@time_it
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result
@time_it          
def cal_cube(numbers):
    result = []
    for number in numbers:
          result.append(number * number * number)
    return result

array = range(1,100000)
out_square = calc_square(array)
out_cube = cal_cube(array)


# In[9]:


"""Generators in python printing fibonaci sequence"""
def fib():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b
        
for f in fib():
    if f > 50:
        break
    print(f)


# In[8]:


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


# In[24]:


"""reading a file and other file operation"""

my_file = open("/users/arnabbasak/Desktop/flask_blog/modi_speech.txt",'r')
example_sent = my_file.read().replace('\n','')
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


# In[25]:


n = int(input("how a=many numbers do you want to create fibonacci series"))
def fib(n):
    a,b = 0,1
    while a < n:
        print(a)
        a,b = b,a+b
    return(a)
print(fib(n))


# In[26]:


message = "meet me tonight."
print(message)
message2 = 'meet me string'
print(message2)
print(message[0:4])
print(message[0:])
print(message[:15])

#srting is immutable


# In[ ]:




