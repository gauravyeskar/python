# shipping fees
cart_total = int(input("Enter the total cart: "))
if(cart_total >=5000):
    print("FREE")
elif(2000 <= cart_total <= 4999):
    print("50 Rs.")
elif(1000 <= cart_total <= 1999):
    print("100 Rs.")
elif(1000 >= cart_total):
    print("150 Rs.")
else:
    print("Invalid Input.")