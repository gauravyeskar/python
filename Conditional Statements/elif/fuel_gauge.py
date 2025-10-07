# fuel indicator
fuel = int(input("Enter the fuel gauge in %: "))
if(75 <= fuel <= 100):
    print("FULL")
elif(50 <= fuel <= 74):
    print("3/4")
elif(25 <= fuel <= 49):
    print("HALF")
elif(24 <= fuel <=10):
    print("LOW")
elif(fuel <=10):
    print("REFUEL")
else:
    print("Invalid Input")