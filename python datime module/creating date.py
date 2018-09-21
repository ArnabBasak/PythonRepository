import datetime
# datetime .date module
d = datetime.date(2017,7,24)# creating the date
print('the date created is',d)
tday = datetime.date.today()# looking for todays date
print('todays date is',tday)
print('todays day is',tday.day) # for only the day
print('Current year is',tday.year) # for only the year
# for week day
print('Week of the day',tday.weekday()) # for weekday() Monday = 0 and Sunday = 6
print ('Week of the day',tday.isoweekday()) # for isoweekday() Monday = 1 and Sunday = 7

#creating time delta that is the set of time 
tdelta = datetime.timedelta(days=7)
print('The date from today is',tday + tdelta) # to look what will be the date 7 days from today
print('the date which was 7 days back from today',tday - tdelta) # to look what was the date 7 days prior today

#date2 = date1 + timedelta
#timedelta = date1 + date2

#calculate the daya remaining in my birthday
bday = datetime.date(2017,9,26)
till_bday = bday - tday
print('days remaining in my birthday from today is',till_bday)
print('days remaining in my birthday from today is',till_bday.days) # To see only the days remaining
print('days remaining in my birthday from today is',till_bday.total_seconds) # to see total seconds remaing
