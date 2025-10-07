tyre = int(input("Enter the number of tyres: "))
if(0 < tyre < 51):
    if(tyre == 1):
         print("Unicycle")
    if(tyre == 2):
        print("It's a bike.")
    if(tyre == 3):
        print("It's Rikshaw.")
    if(tyre == 4):
        print("It's a Car.") 
    if(5 <= tyre <= 50):
        if(tyre %2 == 1):
            print("Invalid. No Such vehicle is designed.")
        else:
            print("Heavy Vehicle.")
else:
    print("Invalid. No such Vehicle is designed.")