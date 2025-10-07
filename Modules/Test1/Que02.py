# User se year input and check for leap year or not and if yes then find day for 29th feb.

import calendar,datetime
yr = int(input("Enter the Year:- "))
if calendar.isleap(yr):
    date = datetime.datetime(yr,2,29)
    day = date.strftime("%A")
    print(f"{yr} is a leap year and day is {day}.")
else: 
    print(f"{yr} is not a leap year.")