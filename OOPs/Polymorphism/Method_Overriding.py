# ================
# POLYMORPHISM:- polymorphism comes from 2 greek words. Ploy=many, morphism=forms.
# ploymorphism uses Method Overriding and method Overriding uses Inheritance.
# ----------------
# Create 2 object by using Overriding method.
'''class C1:
    def disp1(self):    # Overriden method
        print("C1----disp()")
    
class C2():
    def disp1(Self):   # Overriden method
        print("C2----disp()")
        super().disp1()

class C3(C2,C1):
    def disp1(self):   # Overriden method
        print("C3----disp()")
        super().disp1()

obj = C3()
obj.disp1()'''

# Over riding not possible in same class. Only the lastest will be taken at the down most one.
"""class C1:
    def disp(self):
        print("C1---> Disp()")
    def disp(self):
        print("C1---> disp") 

obj = C1()
obj.disp()"""
 
# Method Overriding:-  1.
'''class Add():
    def result(self,a,b):
        print("Addition:= ",a+b)

class Mul(Add):
    def result(self,a,b):
        print("Multi:- ",a*b)
        super().result(a,b)

a = int(input("Enter the first value:- "))
b = int(input("Enter the second Number:- "))
obj = Mul()
obj.result(a,b)'''

# 2. With Constructors:- 
'''class Add():
    def __init__(self): # Original Constructor
        print("Add --->  Constructor..!!")
class Sub(Add): # OverRidden Constructor
    def __init__(self):
        print("Sub --->  Constructor..!!")

class Mul(Sub): # OverRidden Constructor
    def __init__(self):
        print("Mul --->  Constructor..!!")
        super().__init__() #calling the sub constructor.

obj = Mul()'''

# 2. With Constructors and polymorphism:- 
'''class Add():
    def __init__(self): # Original Constructor
        print("Add --->  Constructor..!!")
class Sub(Add): # OverRidden Constructor
    def __init__(self):
        print("Sub --->  Constructor..!!")

class Mul(Sub): # OverRidden Constructor
    def __init__(self):
        print("Mul --->  Constructor..!!")
        Sub.__init__(self) # by using 'Class_name' calling.
        Add.__init__(self)

obj = Mul()'''

# Print the area of circle by using polymorphism and method 
'''class Circle():
    def area(self): # Original method
        self.r = float(input("Enter the Radius:- "))
        self.ac = 3.14*self.r*self.r
        print("The Area of Circle is:- ",self.ac)

class Square(Circle):
    def area(self): # method OverRiding
        self.s = float(input("Enter the Side:- "))
        self.sa = self.s * 2
        print("Area of square is:- ",self.sa)
        print("*"*20)
        super().area()    
    
class Rect(Square):
    def area(self): # method OverRiding
        self.l = float(input("Enter the Length:- "))
        self.b = float(input("Enter the Breadth:- "))
        self.ra = self.l*self.b
        print(f"Area of Rectangle is:- {self.ra}")
        print("*"*20)
        super().area()
        
c = Rect()
c.area()'''

# Print the area's of the following using the multi-level inheritance
'''class Circle:
    def area(self):
        self.r = float(input("Enter the Radius:- "))
        self.ac = 3.14 * self.r * self.r
        print(f"Area of Circle is:- {self.ac}")

class Square:
    def area(self):
        self.s = float(input("Enter the Side :- "))
        self.sa = self.s * 2
        print(f"Area of Square is: {self.sa}")

class Rect(Square,Circle):
    def area(self):
        self.l = float(input("Enter the Length:- "))
        self.b = float(input("Enter the Breadth:- "))
        self.ar = self.l * self.b
        print(f"Area of Rectangle is:- {self.ar}")
        print("*"*20)
        super().area()
        print("*"*20)
        Circle.area(self) #Class name method calling

c = Rect()
c.area()'''

# Print the area's of the following using the multi-level inheritance by constructor.
'''class Circle:
    def __init__(self): #Original Constructor
        self.r = float(input("Enter the Radius:- "))
        self.ac = 3.14 * self.r * self.r
        print(f"Area of Circle is:- {self.ac}")

class Square:
    def __init__(self): #OverRiden Constructor
        self.s = float(input("Enter the Side :- "))
        self.sa = self.s * 2
        print(f"Area of Square is: {self.sa}")

class Rect(Square,Circle):
    def __init__(self): # OverRiden Constructor
        self.l = float(input("Enter the Length:- "))
        self.b = float(input("Enter the Breadth:- "))
        self.ar = self.l * self.b
        print(f"Area of Rectangle is:- {self.ar}")
        print("*"*20)
        super().__init__()
        print("*"*20)
        Circle.__init__(self) #Class name method calling

c = Rect()''' 