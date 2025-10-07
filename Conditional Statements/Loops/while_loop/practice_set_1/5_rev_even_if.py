print("Reverse even number: ")
i = int(input("Enter the starting number: "))
j = int(input("Enter the ending number: "))

while(j >= i):
    if(j % 2 == 0):
        print(j)
    j-=1