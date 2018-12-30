n = int(input("how a=many numbers do you want to create fibonacci series"))
def fib(n):
    a,b = 0,1
    while a < n:
        print(a)
        a,b = b,a+b
    return(a)
print(fib(n))
