import pandas as pd
import numpy as np

# df1 = pd.read_csv('df1.csv')
# df2 = pd.read_csv('df2.csv')
# df = pd.concat([df1,df2])
# df = df.reset_index(drop = True)
# df_grpby = df.groupby(list(df.columns))
# idx = [x[0] for x in df_grpby.groups.values()if len(x) == 1]
# print(idx)


file1 = open('df1.csv','r')
file2 = open('df2.csv','r')
file1data = file1.readlines()
file2data = file2.readlines()
updatefile = ('update.csv','w')
for data in file1:
    if data not in file2:
        updatefile.write(data)
updatefile.close()
updatefile = open('update.csv','r')
data = updatefile.readlines()
for elements in data:
    print(elements)
