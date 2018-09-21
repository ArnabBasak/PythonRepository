# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 13:13:01 2018

@author: Arnab
"""

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
dblist = myclient.list_database_names()
print(dblist)
if mydb in dblist:
    print('Database created successfully')
else:
    print('Database is not created')

