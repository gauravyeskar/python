# Take hours and minutes from user and tell how many hours are remaining to end the day.

from datetime import datetime,timedelta
hrs = int(input("Enter the hours (0-23):- "))
mins = int(input("Enter the Minutes (0-59):- "))

ful_day = timedelta(hours=23, minutes= 59)
current_time = timedelta(hours=int(hrs) , minutes= int(mins))

remaining_hrs = (ful_day(timedelta(hours=hrs))- (current_time(timedelta(hours = hrs))))
print("Remainang hrs:- ",remaining_hrs)