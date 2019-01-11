# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 20:41:10 2018

@author: Arnab
"""
import matplotlib.pyplot as plt
days = [1,2,3,4,5]
sleeping = [7,8,6,11,7]
eating = [2,3,4,3,2]
working = [7,8,7,2,2]
playing = [7,5,8,7,13]

slices = [7,2,2,13]
activities = ['sleeping','eating','working','playing']
cols = ['c','m','r','b']
plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0,0.1,0,0),
        autopct='%1.1f%%')
#plt.xlabel('x')
#plt.ylabel('y')
plt.title('Intersting Graph\nCheck it out')
#plt.legend()
plt.show()
