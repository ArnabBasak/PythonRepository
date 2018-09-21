# more methods on list
say = ['hey','brown','cow','how','are','you']
print(say)

print('the position of brown is',say.index('brown'))
say.pop(1)
print('after poping the 1st element',say)
say.insert(2,'goodlooking')
print('after inserting one element at postion 2',say)
say.remove('cow')
print('after removing and not returning an element',say)
say.reverse()     
print('the reverse of the list is',say)       
