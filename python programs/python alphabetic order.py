# python program for alphabetic order
my_string = input("enter any string")
words  = my_string.split()
words.sort()
for i in words:
    print(i)