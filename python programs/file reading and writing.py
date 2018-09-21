# python program to read the content of a file
import os
filecheck = os.path.isfile('E:\python programs\myfile.txt')
if filecheck == False:
    print('file does not exits')
    print('file created')
    fob = open('E:\python programs\myfile.txt','w+')
    fob.write('hwllo world')
    fob.close()
else:
    fob = open('E:\python programs\myfile.txt', 'r')
    print(fob.read())  # comment out any one of the print statement to see the proper output
    print(fob.readline())
    print(fob.readlines())
    fob.close()
# appending of file
    fob = open('E:\python programs\myfile.txt', 'a')
    entertext = input('enter the text you want to enter in the file\n')
    fob.write(entertext)
    fob.close()
# creatiion of file
    filecheck = os.path.isfile('E:\python programs\irst.txt')
    if filecheck == True:
     print('file already exist')
    else:
        fob = open('E:\python programs\irst.txt', 'w+')
        filetext = input('enter any thing in the file\n')
        fob.write(filetext)
        fob.close()
