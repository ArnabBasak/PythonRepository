#program for calculating armstrong number in an interval
lowerrange = int(input('enter the lower range'))
higherrange = int(input('enter the higher range'))
for num in range(lowerrange,higherrange+1):
    sum = 0
    temp = num
    while temp>0:
        digit = temp %10
        sum +=digit **3
        temp //= 10
    if num == sum:
        print(num)