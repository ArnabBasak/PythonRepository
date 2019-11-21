#print('hello world')
#string variabe python 
#position
a = " Hello All "
print("The charater at postiion 3 is ",a[3])
#substring get the characters from position 2 to 5 
print("The characters from 2 to 5 are ",a[2:5])
#strip method
print(a.strip())
#length of the string 
print("The length of the string is",len(a))
#lower function of the string
print("The lower case of the string is ",a.lower())
#upper function of the string
print("The upper case of the string is " ,a.upper())
#Replace function of the string
print("Replaceing H with L",a.replace("H","L"))
def frange(x,y,jump):
    while x<y:
        yield x
        x+=jump
print(list(frange(0,10,0.1))[-1])
import numpy 
print(type(numpy.arange(0,5,0.1)))

print(numpy.arange(0,4,0.1))
print(numpy.arange(4,6,0.1))
print(numpy.arange(6,8,0.1))
print(numpy.arange(8,10,0.1))
import math
a = 8.5333333
print(math.ceil(a))