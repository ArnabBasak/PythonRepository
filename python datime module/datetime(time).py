import datetime
# datetime.time module
t = datetime.time(22,40,45)
print(t)
timenow = datetime.date.today()
print(timenow)
dt = datetime.datetime.today()
print(dt)
tdelta = datetime.timedelta(days = 7)
print('7 days from today exactly will be',dt + tdelta)
tdelta2 = datetime.timedelta(hours = 12)
print('12 hours from now will be',dt + tdelta2)


