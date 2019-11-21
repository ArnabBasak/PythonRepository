import pandas as pd
from pandasql import sqldf
battingrecords = pd.read_excel('battin.xlsx')
#print(battingrecords)
centuries = "select Centuries from battingrecords where Player_name = 'Tendulkar'"
print(sqldf(centuries,locals()))
totalfiftyplusscore = "select (Centuries + HalfCenturies) from battingrecords where Player_name = 'Tendulkar'"
IndiaCenturylist = list((sqldf(centuries,locals())))
for element in IndiaCenturylist:
    print(element)
#q = "select (((Centuries) / (Centuries + HalfCenturies)) * 100 ) as TOTAL_FIFTY from battingrecords where Country = 'INDIA'"
#print(sqldf(q,locals()))