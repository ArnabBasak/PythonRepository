# HCF calculation using function
# LCM calculation
def HCF(x,y):
    if x>y:
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller + 1):
        if(x%i==0)and(y%i==0):
            hcf= 1
    return hcf
num1 =  int(input('enter number 1'))
num2 = int(input('enter number 2'))
print("the HCF of the given numbers are: ",HCF(num1,num2))
