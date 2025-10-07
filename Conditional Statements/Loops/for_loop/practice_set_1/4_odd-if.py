start = int(input("enter the starting point: "))
end = int(input("Enter the ending point: "))
for start in range(start,end,1):
    if start%2!=0:
        print(start)