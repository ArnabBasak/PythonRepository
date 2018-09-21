# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 23:58:55 2018

@author: Arnab
"""

import json
#==============================================================================
# with open('bowler.json', 'r') as f:
#     distros_dict = json.load(f)
#     print(type(distros_dict))
# for distro in distros_dict:
#     print(distro)
#==============================================================================
homewicketslist = []
awaywicketslist = []
with open('Waqar Younis.json') as wy:
    wydict = json.load(wy)
with open('McGrath.json') as mg:
    mgdict = json.load(mg)
with open('kumble.json') as k:
    kdict = json.load(k)
with open('srinath.json') as s:
    sdict = json.load(s)
with open('Lee.json') as l:
    ldict = json.load(l)
with open("vaas.json") as v:
    vdict = json.load(v)
with open('pollock.json') as p:
    pdict = json.load(p)
with open('jayasuriya.json') as js:
    jsdict = json.load(js)
with open('Wasim Akram.json') as wa:
    wadict = json.load(wa)
with open('Muralitharan.json') as m:
    mdict = json.load(m)
homewicketslist.append(wydict.get("Home"))
awaywicketslist.append(wydict.get("Away"))
homewicketslist.append(kdict.get("Home"))
awaywicketslist.append(kdict.get("Away"))
homewicketslist.append(sdict.get("Home"))
awaywicketslist.append(sdict.get("Away"))
homewicketslist.append(ldict.get("Home"))
awaywicketslist.append(ldict.get("Away"))
homewicketslist.append(vdict.get("Home"))
awaywicketslist.append(vdict.get("Away"))
homewicketslist.append(pdict.get("Home"))
awaywicketslist.append(pdict.get("Away"))
homewicketslist.append(jsdict.get("Home"))
awaywicketslist.append(jsdict.get("Away"))
homewicketslist.append(wadict.get("Home"))
awaywicketslist.append(wadict.get("Away"))
homewicketslist.append(mdict.get("Home"))
awaywicketslist.append(mdict.get("Away"))
maxhomewickets = max(homewicketslist)
maxawaywickets = max(awaywicketslist)
print(maxhomewickets)
print(maxawaywickets)

