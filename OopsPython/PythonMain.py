from StudentClass import *
print('enter 1 for addition\n enter 2 for substraction\n enter 3 for multiplication \n enter 4 for division ')
userchoice = int(input('enter your choice'))
if userchoice == 1:
    a = Addition()
    a.getdata()
    a.calulcate()
    a.display()
elif userchoice == 2:
    s = Substration()
    s.getdata()
    s.calulcate()
    s.display()
elif userchoice == 3:
    m = multiplication()
    m.getdata()
    m.calulcate()
    m.display()
elif userchoice == 4:
    d = division()
    d.getdata()
    d.calulcate()
    d.display()
else:
    print('invalid input')
