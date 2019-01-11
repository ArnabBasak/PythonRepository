# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 20:17:30 2018

@author: Arnab
"""

import matplotlib.pyplot  as plt
#Histogram
population_ages = [22,55,66,45,21,22,34,42,4,102,108,30,49,78,10,65,130,131,38,33,12,18,15,75,95,123,101]
#ids = [x for x in range(len(population_ages))]
bins = [0,10,20,30,40,50,60,80,90,100,110,120,130]
plt.xlabel('x')
plt.ylabel('y')
plt.title('interesting graph\ncheck it out')
plt.hist(population_ages,bins,histype='bar',rwidth=0.8)
