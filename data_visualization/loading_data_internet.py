# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 23:01:09 2018

@author: Arnab
"""

import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates
def graph_data():
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    stock_data = []
    split_source = source_code.split('\n')
    for line in split_source:
        split_line = line.split(',')
        if len(split_line) == 6:
            if "values" not in line:
                stock_data.append(line)
    date,closep,highp,lowp,volume = np.loadtxt(stock_data,
                                               delimiter=',',
                                               unpack=True,
                                               # %Y = full year.2015
                                               # %Y = partial year 15
                                               # %m = number months
                                               # %d = number day
                                               # %H = Hours
                                               # %M = minutes
                                               # %s = seconds
                                               #12-06-2014
                                               # %m -%d -%y
                                               converters={0:bytespdate2num('')})
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Intersting Graph\nCheck it out')
    plt.legend()
    plt.show()
    
