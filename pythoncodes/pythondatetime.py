import datetime 
import calendar
datedict = {"Monday" : 0,
"tuesday": 1,
"wednesday": 2,
"thursday": 3,
"friday": 4,
"saturday": 5,
"sunday": 6}
#print(datetime.datetime.today().weekday())
#my_date = date.today()
#print(calendar.day_name[my_date.weekday()])
#dt = '02/09/2018'
datefile = open('/home/arnab/Desktop/pythoncodes/dates.txt','r')
for dt in datefile:
    day,month,year = (int (x) for x in dt.split('/'))
    ans = datetime.date(year,month,day)
    print(dt, ans.strftime("%A"))
