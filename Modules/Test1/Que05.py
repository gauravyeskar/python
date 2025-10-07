# Take an input as year from user and find total mondays,tuesdays,wednesdays....,saturdays and sundays. and according to the IT sector find the total working days.
import datetime,calendar
def week_workdays(yr):
    sunday,monday,tuesday,wednesday,thursday,friday,saturday=0,0,0,0,0,0,0
    for month in range(1,13):
        month_days = calendar.monthcalendar(yr,month)
        for weeks in month_days:
            for i,day in enumerate(weeks):
                if day != 0:
                    if i ==0:
                        monday +=1 
                    elif i ==1:
                        tuesday+=1
                    elif i ==2:
                        wednesday +=1
                    if i ==3:
                        thursday +=1 
                    elif i ==4:
                        friday +=1
                    elif i ==5:
                        saturday +=1
                    elif i == 6:
                        sunday +=1
    working_days = monday+tuesday+wednesday+thursday+friday
    week_ends = saturday + sunday
    print("*"*30)
    print('Leap Year:- 366 days' if calendar.isleap(yr) else 'not a Leap Year:- 365 days')
    print("*"*30)
    print("Total Sundays:- ",sunday)
    print("Total Mondays:- ",monday)
    print("Total Tuesdays:- ",tuesday)
    print("Total Wednesdays:- ",wednesday)
    print("Total Thursdays:- ",thursday)
    print("Total Fridays:- ",friday)
    print("Total Saturdays:- ",saturday)
    print("*"*30)
    print("Total Working days in IT for year {} is {}".format(yr,working_days))
    print("Total Weekend days in IT for year {} is {}".format(yr,week_ends))
    print("*"*30)

week_workdays(int(input("Enter the year:- ")))