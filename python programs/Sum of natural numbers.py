# python program to find sum of natural numbers
number = int(input('enter any number'))
if number<0:
    print('enter a positive number')
else:
    sum = 0
    while(number>0):
        sum = sum+number
        number = number-1
    print(sum)
