end = int(input("Enter the ending point: "))
start = int(input("Enter the start point: "))
for end in range(end,start,-1):
    if(end%2!=0):
        print(end)