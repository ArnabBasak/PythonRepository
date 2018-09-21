import random
s = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = int(input("enter the length of the password"))
passo = "".join(random.sample(s,passlen))
print(passo)