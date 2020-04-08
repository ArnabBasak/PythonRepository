"""
write a python program to count the number 4 in the given list
"""
my_list = [4,4,1,2,3,4,2,10]
count = 0
for elements in my_list:
    if elements == 4:
        count = count+1
print(count)
