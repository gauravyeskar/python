# SINGLE INHERI :- One Child Class inherits from one Parent Class.
"""
1. User & Authentication Systems:- 
    Here below are 4 programs which clears what actually Single Inheritance means.
"""
'''
class User:
    def __init__(self,username:str,email:str):
        self.username = username 
        self.email = email 
    def check_access(self):
        return "Standard Access"

    def get_data(self):
        print(f"User: {self.username} | Email: {self.email}")

class AdminUser(User):
    def __init__(self, username:str, email:str):
        super().__init__(username, email)
        self.is_super_Admin =  True
    def show_Admin_status(Self):
        print(f"{Self.username} Status: Admin ({Self.is_super_Admin})")
u1 = User("gauravyes","gauyes@.com")
u1.get_data()
print(f"Access Level:- {u1.check_access()}")
print("-"*50)

a1 = AdminUser("Sys Admin","admin@com")
a1.get_data()
a1.show_Admin_status()
'''

# 02: Guest Checkout
'''
class Customer:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
    def show_data(Self):
        return f"{Self.first_name} {Self.last_name}"

class Guest_Customer(Customer):
    def __init__(self):
        super().__init__("Guest","User")

c1 = Customer("Gaurav","Yeskar")
print(f"Customer Name:- {c1.show_data()}")

g1 = Guest_Customer()
print(f"Customer 2:- {g1.show_data()}")
'''

# 03: Digital vs. Physical Product
'''
class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def get_tax_rate(self):
        return 0.07
    
    def get_data(self):
        print(f"Product: {self.name} \nPrice: {self.price}")
    
class DigitalProduct(Product):
    def __init__(self,name,price,link):
        super().__init__(name,price)
        self.link = link

p1 = Product("T-shirt",250)
p1.get_data()
print("Tax Rate: ",p1.get_tax_rate())
print("-"*50)

dp1 = DigitalProduct("E-book",100,"www.google.com")
dp1.get_data()
print("Tax Rate: ",dp1.get_tax_rate())
print("Link: ",dp1.link)
'''

# 04: Basic vs. Premium Shipping
'''
class Shipment:
    def __init__(self,cost):
        self.cost = cost

    def cal_delivery_days(self):
        return 5
    
    def show_data(self):
        print(f"Cost: {self.cost}")

class ExpressShipment(Shipment):
    def __init__(self, cost,carrier):
        self.carrier = carrier
        super().__init__(cost)
    
s1 = Shipment(50000)
s1.show_data()
print("Delivery Days: ",s1.cal_delivery_days())
print("-"*50)

s2 = ExpressShipment(60000,"Raj carriers")
s2.show_data()
print("Carrier: ",s2.carrier)
print("Delivery Days: ",s2.cal_delivery_days())
'''

# Practice Questions
'''class C1:
    def disp1(self):
        print("From class 1")

class C2(C1):
    def disp2(self):
        self.disp1()
        print("From C2")
# main prog
o1 = C2()
o1.disp2()'''


