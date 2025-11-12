import time as t
import datetime 
import calendar as c

print("*"*20)
print("current date and time : ")
print(datetime.datetime.now())

print("*"*20)
print("Only date: ")
print(datetime.date.today())

print("*"*20)
print(" Current time : ") 
print(datetime.datetime.now().time())

print("*"*20)
print("Only Day: ")
print(datetime.date.today().day)

print("*"*20)
print("Only month  in Number: ")
print(datetime.date.today().month)

print("*"*20)
print("Only month in Letter: ")
print(datetime.date.today().strftime("%B"))

print("*"*20)
print("only year: ")
print(datetime.date.today().year)

print("*"*20)
print("Current hours: ")
print(datetime.datetime.now().hour)

print("*"*20)
print("Current minute: ")
print(datetime.datetime.today().minute)

print("*"*20)
print("Current Second: ")
print(datetime.datetime.today().second)

print("*"*20)
print("date with hyphen: ")
print(datetime.datetime.now().strftime("%H-%M-%S"))

print("*"*20)
print("Date with slash: ")
print(datetime.datetime.today().strftime("%m/%d/%y"))
print("*"*20)