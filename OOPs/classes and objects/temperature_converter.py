# Temperature Converter: Create a Temperature class. The 
# constructor should take a celsius value. Add a method 
# to_fahrenheit() that calculates and returns the Fahrenheit 
# equivalent using the formula: $F = C \times 9/5 + 32$.

class Temperature_class():
    def __init__(self,cs):
        self.cs = cs

    def to_fahrenheit(self):
        f = (self.cs * 9/5) + 32
        return f 
cs = float(input("Enter the Celcius:- "))
t1 = Temperature_class(cs)
print(f"Fehrenheit Temperature is:- {t1.to_fahrenheit()}")