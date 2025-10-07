# Current date se 3 din aage or 3 din piche ka date dikhana hai

from datetime import datetime,timedelta
dat = input("Enter the date (DD-MM-YYYY): ")
getdate = datetime.strptime(dat,"%d-%m-%Y").date()
ahead =getdate + timedelta(days = 3)
back = getdate - timedelta(days = 3)

print("Days after 3 days:- ",ahead)
print("Days after 3 days:- ",back)