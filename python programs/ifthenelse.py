year =input('enter any year in yyyy format')
n = int(year)
number = n%4
if number > 0:
    print('the given year is not a leap year')
else:
    print('the given year is a leap year')
