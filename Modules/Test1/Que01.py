# User se Year,Month,Day in numbers as input and find day in name.

import datetime
date = input("Enter the date YYYY-MM-DD format:- ")
date_obj = datetime.datetime.strptime(date,"%Y-%m-%d").date()
day_name = date_obj.strftime("%A")
print("Day is:- ",day_name)