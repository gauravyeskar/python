print("Reverse odd number: ")
i = int(input("Enter the start number: "))
j = int(input("Enter the end number: "))

while(j >= i):
    if(j % 2 == 1):
        print(j)
    j-=1