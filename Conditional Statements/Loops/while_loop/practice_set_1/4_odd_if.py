print("Odd number with if")
start = int(input("Enter the starting number: ")) #1
end = int(input("Enter the ending number: "))  #10

while(start <= end):
    if(start %2 != 0):
        print(start)
    start+=1