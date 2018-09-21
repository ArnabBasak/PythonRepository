# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 20:01:24 2018

@author: Arnab
"""

import pyttsx3
import pandas as pd
from pandasql import sqldf
engine = pyttsx3.init()
#mylist = ['arnab','basak']
#engine.say(mylist)
#engine.runAndWait()
bowler = pd.read_csv('E:/pythonprograms/Akinator/bowlerrecords.csv')
engine.say('welcome to cricket bowling records, check out the fasinating bowler records in history of cricket ')
engine.runAndWait()
userinput = input('waiting for your response\n')
if userinput == 'y':
    highestwickettakerquery = "select Player from bowler where Wkts IN (select max(Wkts) from bowler)"
    Highestwickettaker= sqldf(highestwickettakerquery,locals())
    print(Highestwickettaker)
    engine.say('highest wicket taker in cricket is')
    engine.say(Highestwickettaker)
    engine.runAndWait()
    lowestwicktakerquery = "select Player from bowler where Wkts IN (select min(Wkts) from bowler)"
    Lowestwickettaker = sqldf(lowestwicktakerquery,locals())
    print(Lowestwickettaker)
    engine.say('lowest wicket taker in cricket is')
    engine.say(Lowestwickettaker)
    engine.runAndWait()
    highesteconomyratequery = "select Player from bowler where Econ IN(select max(Econ) from bowler)"
    Highesteconomyrate = sqldf(highesteconomyratequery,locals())
    print(Highesteconomyrate)
    engine.say('bowler who has highest economy is')
    engine.say(Highesteconomyrate)
    engine.runAndWait()
    lowesteconomyratequery = "select Player from bowler where Econ IN(select min(Econ) from bowler)"
    Lowesteconomyrate = sqldf(lowesteconomyratequery,locals())
    print(Lowesteconomyrate)
    engine.say('bowler who has lowest econmy rate is')
    engine.say(Lowesteconomyrate)
    engine.runAndWait()
    lowestaveragequery = "select Player from bowler where Ave IN(select min(Ave) from bowler)" 
    Lowestaverage = sqldf(lowestaveragequery,locals())
    print(Lowestaverage)
    engine.say('bowler who has lowest average is')
    engine.say(Lowestaverage)
    engine.runAndWait()
    highestaveragequery = "select Player from bowler where Ave IN(select max(Ave) from bowler)"
    Highestaverage = sqldf(highestaveragequery,locals())
    print(Highestaverage)
    engine.say('bowler who has highest average is')
    engine.say(Highestaverage)
    engine.runAndWait()
    higheststrickratequery = "select Player from bowler where SR IN(select max(SR) from bowler)"
    Higheststrickrate = sqldf(higheststrickratequery,locals())
    print(Higheststrickrate)
    engine.say('highest strike rate is')
    engine.say(Higheststrickrate)
    engine.runAndWait()
    loweststrickratequery = "select Player from bowler where SR IN(select min(SR) from bowler)"
    Loweststrickrate = sqldf(loweststrickratequery,locals())
    engine.say('bowler with lowest strike rate is')
    engine.say(Loweststrickrate)
    engine.runAndWait()
    mostbowlbowledquery = "select Player from bowler where balls IN(select max(balls) from bowler)"
    Mostbowlbowled = sqldf(mostbowlbowledquery,locals())
    print(Mostbowlbowled)
    engine.say('the bowler who bowled most balls')
    engine.say(Mostbowlbowled)
    engine.runAndWait()
    leastbowledquery = "select Player from bowler where balls IN()"
    
else:
    engine.say('oh ok thanks have a great day')
    engine.runAndWait()
