# Take a date from user and module will tell that after how many days after the sunday is there.
from datetime import datetime,date,timedelta
def day_sunday(): 
    yr = int(input("Enter the Year (YYYY):- "))
    month = int(input("Enter the month (1-12):- "))
    day = int(input("Enter the Day date (1-31):- "))
    getdata = date(yr,month,day)
    print("*"*30)
    day_index = getdata.weekday()
    sunday = 6- day_index
    next_sunday = getdata + timedelta(days= sunday)

    print(f"The date you entered is: {getdata.strftime('%A, %B %d, %Y')}")
    print(f"Days until the next Sunday: {sunday}")
    print(f"That Sunday will be on: {next_sunday.strftime('%B %d, %Y')}")
    print("*"*30)
day_sunday()