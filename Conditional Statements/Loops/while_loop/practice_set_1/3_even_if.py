print("Even number with if")
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

while(start <= end):
    if(start %2 == 0):
        print(start)
    start+=1