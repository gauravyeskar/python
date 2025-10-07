print("user even with no if")
start=int(input("Enter the first number: "))
end=int(input("Enter the end number: "))
start+=start%2
i=start
while(i <= end):
    print(i)
    i+=2