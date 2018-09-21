# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 19:23:04 2017

@author: Arnab
"""

import pandas as pd
from pandasql import sqldf
mymoviedataframe = pd.read_csv('MovieNames.csv')
#print(mymoviedataframe)
genre = "select DISTINCT genre from mymoviedataframe;"
genereoutput = sqldf(genre,locals())
print("You have watched ",len(genereoutput),"different genre of flims this year")
language = "select language from mymoviedataframe;"
languageoutput = sqldf(language,locals())
print(languageoutput)


