list1 = ['a','b','c']
print('the list 1 is',list1)
pyset1 = set(list1)
print('the list 1 after converting into set ',pyset1)
list2 = ['a','c','d']
print('the list 2 is',list2)
pyset2 = set(list2)
print('the list 2 after converting into set ',pyset2)
totalset1 = pyset1 - pyset2
print('elements present only in set 1',totalset1)
totalset2 = pyset2 - pyset1
print('elements present only in set 2',totalset2)
intersectionset = pyset1 & pyset2
print('elements present in both the set',intersectionset)
