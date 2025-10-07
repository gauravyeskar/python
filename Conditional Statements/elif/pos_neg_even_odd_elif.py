#positive and even odd number by elif:
a = int(input("Enter the number: "))
if(a > 0 and a % 2 == 0):
    print("The number is positive and even number.")
elif(a > 0 and a % 2 == 1):
    print("The number is positive and odd number.")
elif(a < 0 and a % 2 == 0):
    print("The number is negative and even number.")
else:
    print("The number is negative and odd number.")
