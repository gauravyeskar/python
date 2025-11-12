# Vehicle Registration: Design a Vehicle class. The constructor 
# should take make, model, and year. Add a method 
# get_description() that returns a formatted string 
# like: "2023 Toyota Camry"..

class Vehicle:
    def __init__(self,owner,model,year):
        self.owner = owner
        self.model = model
        self.year = year
    def get_data(self):
        return f"{self.year} {self.model} {self.owner}"


owner = input("Enter Owner Name of Car:- ")
Model = input("Enter the Model of Car:- ")
Year = int(input("Enter the Year Of Car:- "))
v1 = Vehicle(owner,Model,Year)
description =v1.get_data()
print(f"Car Description :- {description}")