# 5
'''
Problem Statement and Explanation
In this problem, we will learn the difference between class and instance using object-oriented programming. we will return the following string based on the following conditions:

If the age is 0 or less, we will print Age is not valid, setting age to 0. and set the age to 0.
There are 3 conditions to check the age:
If the age is less than 13, we will print You are young.
If the age is greater than or equal to 13 and less than 18, we will print You are a teenager.
Otherwise, we will print You are old.
'''
'''class Person:
    def __init__(self,initialAge):
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
            self.age = 0
        else:
            self.age = initialAge      
    def amIOld(self):
        if self.age <13:
            print("You are young.")
        elif self.age >=13 and self.age<18:
            print("You are a teenager.")
        else:
            print("You are old.")
    def yearPasses(self):
        self.age += 1
t = int(input("Enter the Number:- "))
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")  '''

##########################################################################################################################
# Day-5:- Loop
# Print the table using loop
n = int(input("Enter the Number:- "))
for i in range(1,11):
    print(n,"X",i,'=',n*i)