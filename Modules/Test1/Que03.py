# User se date of birth as input and find the users age in years months and days.

from datetime import datetime
date_val = int(input("Enter the date:- "))
month_val = int(input("Enter the month:- "))
year_val = int(input("Enter the Year:- "))

a = datetime(year_val, month_val, date_val) 

today = datetime.now() 

age_year_diff = today.year - a.year if today.year >  a.year else a.year - today.year 
age_month_diff = today.month - a.month if today.month > a.month else a.month - today.month
age_day_diff =  a.day - today.day if a.day > today.day else today.day - a.day
print("Year: {}, Month: {}, Day : {}".format(age_year_diff, age_month_diff, age_day_diff))