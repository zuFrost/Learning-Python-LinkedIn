# Which code can you use to print a standard, text-formatted monthly calendar for every month 
# in 2020, using Sunday as the first day of the week?


# import calendar
# for m in range(1,13):
#     cal = calendar.monthcalendar(2020,m)
#     print(cal)


# import calendar
# cal = calendar.TextCalendar(calendar.SUNDAY)
# for m in range(1,13):
#     print(cal.formatmonth(2020, m, 0, 0))


# import calendar
# cal = calendar.monthcalendar(2020)
# print(cal.formatmonth(calendar.SUNDAY))


# import calendar
# cal = calendar.TextCalendar(calendar.SUNDAY)
# for m in range(1,12):
#     print(cal.formatmonth(2020, m))

# Given that now=datetime.now(), which call may produce different results on different computers?
# import datetime


# now = date.today()


# print(now.strftime("%d"))


# print(now.strftime("%Y"))


# print(now.strftime("%M"))


# print(now.strftime("%c"))

# What should come instead of the ??? placeholders for this code 
# to correctly print the number of days until your birthday on Jun 30? 
# Hint: the number of days in a timedelta object can be returned using its days attribute.
# from datetime import date
# # from datetime import time
# # from datetime import datetime

# today=date.today()
# bday=date(today.year,6,30)
# diff=(bday-today).days
# if diff>0:
#   print("Birthday in %d days" % diff)
# else:
#   print("Birthday in %d days" % (diff+365))

  
# (bday-today).days; diff+365

# (bday-today).days+365; diff

# bday-today; 365-diff

# bday.days-today.days; diff+365




# You need to calculate tomorrow's date. Which option should you choose?
# from datetime import date
# from datetime import timedelta

# today=date.today()
# # Option A:
# tomorrow=today+timedelta(days=1)
# print(tomorrow)
# # Option B:
# tomorrow2=date(today.year,today.month,today.day+1)
# print(tomorrow2)


# You create a simple calendar program that needs to print tomorrow's day of the week. 
# Which code will work under all circumstances?


# today=date.today()
# days=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
# print("Tomorrow will be "+days[(today.weekday()+1])


# today=date.today()
# days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
# print("Tomorrow will be "+days[(today.weekday()+1)%7])


# today=date.today()
# days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
# print("Tomorrow will be "+days[today.weekday()+1])


# today=date.today()
# days=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
# print("Tomorrow will be "+days[(today.weekday()+1)/7])

# Which call will return the same result like date.today()?

from datetime import date
from datetime import datetime

date.today()
print(date.today())

# 1
# datetime(date.today())
# print(datetime(date.today()))

# 2
datetime.date(datetime.now())
print(datetime.date(datetime.now()))
# 3
# datetime.time(datetime.now)
# print(datetime.time(datetime.now))
# 4
# datetime.date()
# print(datetime.date())