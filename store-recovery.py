# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 22:34:29 2018

@author: Arnab
"""

import pymysql
import csv

#connecting to the database
connworld =  pymysql.connect(host = "localhost",user = "root",password = "baban123",db = "store")

#selecting data and writing the data in the csv files for the customers
curcity_world = connworld.cursor()
curcity_world.execute("select * from releasedates")
resultcity_world = curcity_world.fetchall()
myfilecity_world = csv.writer(open('E:/pythonprograms/release_dates.csv','w',encoding = 'utf-8'))
col_names = [i[0] for i in curcity_world.description]
myfilecity_world.writerow(col_names)
myfilecity_world.writerows(resultcity_world)
print("release_dates.csv file has been written")


#this is to check the counts
userinput = input ('enter the date to check')
curcity_world.execute("SELECT count(*) FROM releasedates WHERE rolloutdate LIKE %s",(userinput))
answer = curcity_world.fetchall()
finaloutput = "total number of store upgraded" + str(answer)
reportfile = open('outputfile.txt','w')
reportfile.write(finaloutput)
reportfile.close()
#analysis_file = open('analysis_file','a')
#analysis_file.write(answer)
 