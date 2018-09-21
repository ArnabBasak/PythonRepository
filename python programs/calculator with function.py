#program to create calculator using function
def add(x,y):
    z = x+y
    print('addition is: ',z)
def sub(x,y):
    z = x+y
    print('substraction is: ',z)
def mul(x,y):
    z = x*y
    print('multiplication is: ',z)
def div(x,y):
    z = x/y
    print('division is: ',z)

num1 = int(input("enter number 1"))
num2 = int(input("enter number 2"))
choice =  int(input('enter your choice\npress 1 for addition: \npress 2 for substraction: \npress 3 for multiplication: \npress 4 for division '))
if choice == 1:
    add(num1,num2)
elif choice == 2:
    sub(num1,num2)
elif choice == 3:
    sub(num1,num2)
elif choice == 4:
    sub(num1,num2)
else:
    print('invalid options')
