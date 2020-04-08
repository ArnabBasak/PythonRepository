import numpy as np
import math
x1 = np.array([1,2,3,4,5,6,7,8,9])
x2 = np.array([10,12,14,16,17,19,21,23,24])
y1 = np.array([-5,-4,-3,-2,-1,0,1,2,3])
y2 = np.array([-11,-10,-9,-8,-7,-6,-5,-4,-3])

x = (x1-x2)**2
y = (y1-y2)**2

print(np.sqrt(x+y))
