mtr_bill = int(input("Enter the meter Unit of electricity: "))
if(0 <= mtr_bill <= 100):
    print("Your bill is: ",mtr_bill*1,"Rs.")
    
elif(101 <= mtr_bill <= 200):
    print("Your Bill is: ",mtr_bill*2,"Rs.")
    
elif(201 <= mtr_bill <= 300):
    print("Your Bill is: ",mtr_bill*3,"Rs.")
    
elif(301 <= mtr_bill <= 400):
    print("Your Bill is: ",mtr_bill*4,"Rs.")
    
elif(401 <= mtr_bill <= 500):
    print("Your Bill is: ",mtr_bill*5,"Rs.")
    
else:
    print("Your Bill is: ",mtr_bill*7,"Rs.")
