print("Reverse odd without if")
start = int(input("Enter the starting number: ")) #1
end = int(input("Enter the ending number: ")) #10
i=start
while(i>=end and i%2!=0):
    print(i)
    i-=2