# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 20:21:23 2018

@author: Arnab
"""

import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7,8]
y = [5,2,4,3,8,1,7,10]
plt.scatter(x,y,label='scatterr',color='r',marker='*',s=500)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Intersting Graph\nCheck it out')
plt.legend()
plt.show()