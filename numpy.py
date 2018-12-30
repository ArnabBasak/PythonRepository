#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 23:56:40 2018

@author: arnabbasak
"""

import numpy as np
import sys
import time
l = range(1000000000)
print(sys.getsizeof(1)*len(l))
array = np.arange(1000)
print(array.size*array.itemsize)

SIZE = 1000
l1 = range(SIZE)
l2 = range(SIZE)
a1 = np.arange(SIZE)
a2 = np.arange(SIZE)

#python list
start = time.time()
result = [(x + y) for x,y in zip(l1,l2)]
print('python list took',(time.time()-start)*1000)

#numpy 
start = time.time()
result = a1 + a2
print('python numpy took',(time.time()-start)*1000) 

#addition
array1 = np.arange(500)
array2 = np.arange(500)
print('addition is',array1 + array2)
print('multiplication is',array1 * array2)