import datetime
import os
filecheck = os.path.isfile('E:\python programs\dates.txt')
if filecheck == False:
    print('sorry file')
elif os.stat('E:\python programs\dates.txt').st_size == 0:
    print('Sorry the file is empty')
else:
    filelines = []
    fileopen = open('E:\python programs\dates.txt','r')
    for line in fileopen:
         line = line.strip()
         filelines.append(line)
    print(filelines)
    print(type(filelines))
    print(len(filelines))
    #filecontents = fileopen.read()
    #print(filecontents)
    
