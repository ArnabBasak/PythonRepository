# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 14:26:57 2018

@author: Arnab
"""

import numpy as np
import matplotlib.pyplot as plt

#make the data
x = np.linspace(0,5)
y = np.exp(x)
print(x,y)

#plot the data 
fignum = 1
plt.close(fignum)
plt.figure(fignum)
plt.plot(x,y)
plt.show()
