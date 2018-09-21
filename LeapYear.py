#leap Year
youryear = int(input('enter the year which you waant to check'))
if youryear%4 == 0:
    if youryear%100 ==0:
        if youryear%400 ==0:
            print('the inputed year is a leap year')
        else:
            print("the inputed year is not a leap year")
    else:
        print("the inputed year is not a leap year")
else:
    print("the inputed year is not a leap year")