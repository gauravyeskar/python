total_days = int(input("Enter the number of days: "))

month = total_days//30
print("The number of month here is: ", month)

mon_rem = total_days%30

weeks = mon_rem // 7
print("The number of weeks here is: ",weeks)

days = mon_rem % 7
print("The number of days is: ", days)


