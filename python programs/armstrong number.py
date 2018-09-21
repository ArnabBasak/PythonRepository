# program for amstrong number
number = int(input("enter any number"))
sum = 0
temp = number
while temp>0:
    digit = temp%10
    sum+=digit**3
    temp //=  10

if number == sum:
    print('the given number is armstrong')
else:
    print('the given number is not armstrong')
