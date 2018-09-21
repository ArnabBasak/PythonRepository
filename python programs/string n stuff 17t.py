variable = "hey %s how are you, how is the %s"
print('the orignal statement is',variable)
var = input('enter any persons name')
thing = input('enter any thing name')
var1 = (var,thing)

print('the modified statement is',variable % var1)

exmple = input('enter a statement')
print(exmple)
tofind = input('enter any word from your statement')
print(exmple.find(tofind))
