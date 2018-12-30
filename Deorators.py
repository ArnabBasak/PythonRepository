#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 22:52:32 2018

@author: arnabbasak
"""

import time
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__+" took "+str((end-start)*1000) + "miliseconds")
        return result
    return wrapper
@time_it
def calc_squares(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result
@time_it
def calc_cubes(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return number
array = range(1,100000)
out_square = calc_squares(array)
out_cubes = calc_cubes(array)