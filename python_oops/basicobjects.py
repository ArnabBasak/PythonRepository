import mymodule
from decimal import Decimal
print(Decimal('3.5') + Decimal('3.5'))
myint = 5
mystr = 'Hello'
mylist = ['a','b','c','d']
mybool = True
mynone = None
def myfunc():
    print('hello from myfunc')
print(type(myint))
print(type(mystr))
print(type(mybool))
print(type(myfunc))
print(type(mynone))
this_type = type(mylist)
print(type(this_type))
var = 5
print(dir(var))
print("numerator of the variable: ",var.numerator)
print("denominator of teh variable: ",var.denominator)
print("number of bit required to store: ",var.bit_length())
print(var.real)
print()
print('these are the data from mymodule')
print(mymodule.dothis())
print(mymodule.myvar)