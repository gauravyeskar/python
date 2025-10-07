# calculate the total days from the users date of birth till now

from datetime import datetime,date,timedelta
dob = input("Enter the Date Of Birth (DD-MM-YYYY) :- ")
date = datetime.strptime(dob,"%d-%m-%Y").date()
current_date = datetime.now().date()
diff = abs(date - current_date)
print(date)
print(current_date)
print(diff)