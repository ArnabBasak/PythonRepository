num = int(input('enter any number'))
if num == 2:
    print(num,'is a prime number')
if num > 1:
    for i in range (2,num):
        if(num % i) == 0:
            print(num,'is not a prime number')
            print(i,'times',num//i,'is',num)
            break
        else:
            print(num,'is a prime number')
            break
else:
    print(num,'is not prime')
        
