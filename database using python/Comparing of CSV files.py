import csv
import itertools
reader1 = csv.reader(open('E:/Python programs/database using python/temp.csv', 'rb'))
reader2 = csv.reader(open('E:/Python programs/database using python/temp2.csv', 'rb'))

for lhs, rhs in itertools.zip(reader1, reader2):
    if lhs != rhs:
        print ("difference:", lhs, rhs)
