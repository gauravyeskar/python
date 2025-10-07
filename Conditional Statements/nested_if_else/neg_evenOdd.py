n = int(input("Enter the number: "))
if(n > 0):
    if(n%2 ==0):
        print(n," is a positive and even number.")
    else:
        print(n," is a positive and odd number")
else:
    if(n % 2 == 0):
        print(n," is a negative and even number.")
    else: 
        print(n," is a negative and odd number")