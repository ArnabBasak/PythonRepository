# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 22:48:40 2018

@author: Arnab
"""

import matplotlib.pyplot as plt
#part 1
"""import csv
x = []
y = []
with open('example.txt','r') as csvfile:
    plots = csv.reader(csvfile,delimiter=',')
    for row in plots:
        x.append(int (row[0]))
        y.append(int (row[1]))
plt.plot(x,y,label='loaded from a file')"""
#part 2
import numpy as np
x,y = np.loadtxt('example.txt',delimiter=',',unpack=True)
plt.plot(x,y,label='loaded from a file')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Intersting Graph\nCheck it out')
plt.legend()
plt.show()
