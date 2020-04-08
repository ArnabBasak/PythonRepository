def FindFeb(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n > 2:
        return FindFeb(n-1) + FindFeb(n-2)
    else:
        print("invalid input")

print(FindFeb(9))
