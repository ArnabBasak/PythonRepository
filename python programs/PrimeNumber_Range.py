lowerlimit=int(input("enter the lower limit"))
upperlimit = int(input("enter the higher limit"))
for num in range(lowerlimit,upperlimit+1):
    if num>1:
        for i in range(2,num):
            if(num%i) == 0:
                break
        else:
            print(num)
