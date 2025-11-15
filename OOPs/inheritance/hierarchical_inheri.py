# Scenario: Vehicle Registration System
class Vehicle:
    def __init__(self,res_num, own_nm):
        self.res_num = res_num
        self.own_nm = own_nm

    def disp_veh(self):
        print(f"Registration Number:- {self.res_num}\nOwner Name:- {self.own_nm}")

class Car(Vehicle):
    def __init__(self,reg_num,own_nm,num_seats,body_style):
        super().__init__(reg_num,own_nm)
        self.num_seats = num_seats
        self.body_style = body_style

    def disp_car(self):
        print(f"----------Car Record----------")
        self.disp_veh()
        print(f"Seats:- {self.num_seats}\nBody_Style:- {self.body_style}")

class Truck(Vehicle):
    def __init__(self, res_num, own_nm,capacity,trailer):
        super().__init__(res_num, own_nm)
        self.capacity = capacity
        self.trailer = trailer
    
    def disp_truck(self):
        print(f"----------Truck Details----------")
        self.disp_veh()
        print(f"Capacity:- {self.capacity}\nTrailer:- {'yes' if self.trailer else 'no'}")

res_num = input("Enter the Registration Number:- ")
own_nm = input("Enter the Owner Name:- ")
seats = int(input("Enter the number of seats of Vehicle:- "))
style = input("Enter the body style:- ")
c1 = Car(res_num,own_nm,seats,style)
t1 = Truck(res_num,own_nm,seats,style)
print("------Hirerarchical--------")
c1.disp_car()
print("\n"+"-"*30 + "\n")
t1.disp_truck()