#To find the factorial of a number
num = int(input("enter the number"))
f = 1
if num <0:
    print("sorry the factorial of negative number doesn't exits")
elif num == 0:
    print("factorial of 0 is either 0 or 1")
else:
    for i in range(1,num + 1):
        f = f*i
    print(f)