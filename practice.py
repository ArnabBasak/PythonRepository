"""def solution(S):
    Bcount = 0
    Acount = 0
    Ncount = 0
    Ocount = 0
    Lcount = 0
    for elements in S:
        if "B" in elements:
            Bcount += 1
        if "A" in elements:
            Acount += 1
        if "N" in elements:
            Ncount += 1
        if "L" in elements:
            Lcount += 1
        if "O" in elements:
            Ocount += 1
    if Bcount == Ncount == Acount and Lcount % 2 == 0 and Ocount % 2 == 0:
        print("BALLOON is possible",Bcount,"times")
    else:
        print("BALLOON not possible from the inputted string")
solution("BALLOONBALLOONBALLOONBALLOON")"""



"""number = int(input('enter a number to find'))
nums = list(range(0,1000))
#print(nums)
if number in nums:
    print("Yes")
else:
    print("No")"""

"""mysentence = "It is a pleasent day today"
res = mysentence.split(" ")
even = 0
evenlist = []
longestword = 0
for elements in res:
    if len(elements) % 2 == 0:
        even += 1
        evenlist.append(elements)
sortedlist = sorted(evenlist,key=len)
print(sortedlist[-1])"""

mystring = "This is my string"
res = mystring.split(" ")
secondstring = "This is my second string"
res2 = mystring.split(" ")
result = set(res) & set(res2)
print(result)
