import calendar

# To print the weekdays of the calendar 
print(calendar.weekheader(4))

#To print the first day of the week
print(calendar.firstweekday())

# To print the calendar of the particular month
print(calendar.month(2019,3))

# To print the whole calendar of the year
print(calendar.calendar(2021))

# To print the day in the month of the calendar
day_of_the_week = calendar.weekday(2021,7,7)
print(day_of_the_week)

# To check whether its a leap or not
is_leap = calendar.isleap(2020)
print(is_leap)

