print("user odd with no if")
i = int(input("Enter the first value: "))
j = int(input("Enter the end value: "))
if(i%2!=0):
    while(i <= j):
        print(i)
        i+=2
else:
    print("Please enter odd number.")
    