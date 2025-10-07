import time
print(time.strftime("%a"))  # Returns week days in short
print(time.strftime("%A"))  # returns week days in long
print(time.strftime("%b"))  # returns month name in short
print(time.strftime("%h"))  # ------------||------------
print(time.strftime("%B"))  # returns month name in long
print(time.strftime("%c"))  # returns week month date time year in short
print(time.strftime("%C"))  # Returns the return century
print(time.strftime("%d"))  # returns the current date
print(time.strftime("%D"))  # Returns whole current date
print(time.strftime("%x"))  # Returns current date 
print(time.strftime("%e"))  # returns current date
# ## print(time.strftime("%E"))  Error
# ## print(time.strftime("%f"))  ValueError
print(time.strftime("%F"))  # returns date in YYYY-MM-DD format
print(time.strftime("%g"))  # return current year
print(time.strftime("%G"))  # Return current Full year
print(time.strftime("%H"))  # returns time in 24-hours 
# ## print(time.strftime("%i"))  ValueError
print(time.strftime("%I"))  # Returns time in 12 hrs
print(time.strftime("%j"))  # Returns day of year 279/365
## print(time.strftime("%J"))  Value Error
## print(time.strftime("%k"))  # ValueError
## print(time.strftime("%K"))  ValueError
## print(time.strftime("%L"))  ValueError
print(time.strftime("%m"))  # Returns month in decimal
print(time.strftime("%M"))  # Returns minute
print(time.strftime("%n"))  # Returns new line
## print(time.strftime("%N"))  ValueError
## print(time.strftime("%O"))  ValueError
print(time.strftime("%p"))  # Returns AM/PM
## print(time.strftime("%P")) ValueError
## print(time.strftime("%q"))  ValueError
print(time.strftime("%r"))  # Returns current time with AM/PM
print(time.strftime("%R"))  # Returns current time without second 
## print(time.strftime("%s"))  # ValueError
print(time.strftime("%S"))  # Returns current Second of time
print(time.strftime("%t"))  # Returns tab
print(time.strftime("%T"))  # Returns current time with seconds
print(time.strftime("%X"))  # Returns current time 
print(time.strftime("%u"))  # Returns week day in number
print(time.strftime("%U"))  # Returns Week From the total year
print(time.strftime("%V"))  # 
print(time.strftime("%w"))  # Returns weekday in numbers
print(time.strftime("%W"))  # Returns current time with AM/PM
print(time.strftime("%y"))  # Returns current year 25
print(time.strftime("%Y"))  # Returns current year 2025
print(time.strftime("%z"))  # Returns current time 
print(time.strftime("%Z"))  # Returns current time Zone Name
print(time.strftime("%%"))  # Returns % Symbol 