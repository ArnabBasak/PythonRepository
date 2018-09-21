# python program to play around with string
mystring = "hello wonderfull people,@#$, '112341,,,;"
print(len(mystring))
removal = ''.join(e for e in mystring if e.isalnum())
print('the string after the removal of the puncutation marks\n',removal,'\nthe length of the string now is',len(removal))
alphabetts = ''.join(e for e in removal if not e.isdigit())
print('the alphabets present in the string are:\n',alphabetts,'\n number of albhabets are:',len(alphabetts))
numbers = ''.join(e for e in removal if not e.isalpha())
print('the digits present in the string are\n',numbers,'\n the number of digits are',len(numbers))
specialcharacter = ''.join(e for e in mystring if not e.isalnum())
print(specialcharacter)