#python program to seperate CSV file
import os
fileexits = os.path.isfile('J:\python programs\mycsv.csv')
if fileexits == True:
    if os.stat('J:\python programs\mycsv.csv').st_size == 0:
        print('sorry the file is empty')
    else:
        fob = open('J:\python programs\mycsv.csv','r')
        fileread = fob.read()
        print('their are ',len(fileread),'characters present in the file')
        speacialcharacters = ''.join(e for e in fileread if not e.isalnum())
       # print('the special characters in the file are',speacialcharacters)
        speacialcharactersfob = open('j:\python programs\specialcharacters.txt','w')
        speacialcharactersfob.write(speacialcharacters)
        print('special character file created')
        speacialcharactersfob.close()
        print('the number of special characters are',len(speacialcharacters))
        #this is to remove the special characters from the csv file
        removal = ''.join(e for e in fileread if e.isalnum())
        #print(removal)
        alpabets = ''.join(e for e in removal if not e.isdigit())
        alpabetsfob = open('j:\python programs\lphabets.txt','w')
        alpabetsfob.write(alpabets)
        print('alphabets file is created')
        alpabetsfob.close()
        lowercase = sum(1 for c in alpabets if c.islower())
        print('the number of lower case letters in the file are',lowercase)
        uppercase = sum(1 for c in alpabets if c.isupper())
        print('the number od upper case letters in the file are',uppercase)
        #print('the alphabets present in the file are',alpabets)
        print('the number of alphabets present in the file are,',len(alpabets))
        digits = ''.join(e for e in removal if not e.isalpha())
        digitsfob=open('j:\python programs\digits.txt','w')
        digitsfob.write(digits)
        print('digits file is created')
        digitsfob.close()
        print('the number of digits present in the file are',len(digits))
        fob.close()
else:
    print('sorry file doesnt exits')


