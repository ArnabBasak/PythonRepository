# reading a text file and making it to csv file
import os
import string
filexits = os.path.isfile('J:\python programs\mycsv.txt')
if filexits == False:
    print('file not exits')
else:
    fob = open('J:\python programs\mycsv.txt','r')
    reading = fob.read()
    #print(reading)
    fob.close()
    filexits = os.path.isfile('J:\python programs\mycsv.csv')
    if filexits == True:
        print('file already exists')
       # print(reading)
    else:
        fob = open('J:\python programs\mycsv.csv','w+')
        fob.write(reading)
        print('file created')
        fob.close()
