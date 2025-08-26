# User salary using AND
sal = int(input("Enter the current salary: "))
age = int(input("Enter your age: "))
if(sal >= 10000 and age >=30):
    print("Your updated salary is: ",sal+1000)
else:
    print("Your updates salary is: ",sal+500)


# User salary using OR
sal = int(input("Enter your current salary: "))
age = int(input("Enter your age: "))
if(sal >=10000 or age > 30):
    print("Your updated salary is ",sal+1000)
else:
    print("Your updated salary is ",sal+500)
