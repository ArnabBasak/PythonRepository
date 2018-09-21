#program to compare two numbers using function
def compare(x,y):
    if x>y:
        print(x,'number is greater')
    elif y>x:
        print(y,'number is greater')
    else:
        print('both the numbers are equal')

number1 = int(input('enter number 1'))
number2 = int(input('enter number 2'))
compare(number1,number2)