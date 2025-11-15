# Multi-Level Inheritance:- 
'''class C1:
    def getA(self):
        self.a = 10
class C2(C1):
    def getB(self):
        self.b = 20
class C3(C2):
    def getC(self):
        self.c = 30
    def operations(self):
        self.getA()
        self.getB()
        self.getC()
        self.d = self.a + self.b + self.c 
        print(self.d)
o1 = C3()
o1.operations()'''

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age,employee_id,salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary
class Professor(Employee):
    def __init__(self, name, age, employee_id, salary,department,courses):
        super().__init__(name, age, employee_id, salary)
        self.department = department
        self.courses = courses
    def disp(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Employee_id: ",self.employee_id)
        print("Salary",self.salary)
        print("Department: ",self.department)
        print("Course: ",self.courses)
name = input("Enter the name:- ")
age = int(input("Enter the age:- "))
employee_id = str(input("Enter the Employee_id:- "))
salary = float(input("Enter Employee Salary:- "))
department = input("Enter the Department:- ")
courses = ['Java','Python','SQL','Data']
p = Professor(name,age,employee_id,salary,department,courses)
p.disp()