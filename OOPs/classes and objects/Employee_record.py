# Employee Record: Create an Employee class. The constructor 
# takes name and salary. Add a class attribute named 
# raise_percentage set to 1.05 (5% raise). Add a method 
# apply_raise() that updates the instance's salary using the
#  class attribute.
class Employee:
    raise_percent = 1.05
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def apply_raise(self):
        self.salary += Employee.raise_percent
        return self.salary

name = input("Enter the Name:- ")
salary = float(input("Enter the Salary:- "))
e1 = Employee(name,salary)
print('Updated Salary:- ',e1.apply_raise())