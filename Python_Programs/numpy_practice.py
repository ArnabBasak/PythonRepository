import numpy as np

print("a_list = [1,2,3,4]")
print("a_array = np.array([1,2,3,4])")

a_list = [1,2,3,4]
a_array = np.array([1,2,3,4])


print("adding the list that is a_list + a_list")
print("a_list+a_list") #it concatenates
print(a_list+a_list)
print()
print("adding the array")
print(a_array + a_array)


print("squaring elements in list")
print([x ** 2 for x in a_list ])

print("squaring elements in array")
print(a_array**2)

print(np.sqrt(a_array))
print(np.log(a_array))
print(np.exp(a_array))
