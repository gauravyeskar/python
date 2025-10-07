#age group
age = int(input("Enter the age: "))
if(age < 13):
    print("Child")
elif(13 > age < 19):
    print("Teenager")
elif(20 > age < 59):
    print("Adult")
elif(60 > age < 79):
    print("Senior")
else:
    print("Super-Senior")