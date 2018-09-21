#this is a slicing exxample
example = list('arnabdas')
print('the list contains',example)
example[5:] = list('basak')
print('the list contains',example)
example2=[7,8,9]
print("the second list is",example2)
example2[1:1] = [3,3,3]
print('the second list after modification is',example2)
example2[1:5] = []
print("after deletion of the list",example2)
