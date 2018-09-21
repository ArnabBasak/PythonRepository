# LCM calculation
def LCM(x,y):
    if x>y:
        greater = x
    else:
        greater = y
    while(True):
        if(greater % x == 0) and (greater % y ==0):
            lcm = greater
            break
        greater+=1
    return lcm

num1 =  int(input('enter number 1'))
num2 = int(input('enter number 2'))
print("the lcm of the given numbers are: ",LCM(num1,num2))
