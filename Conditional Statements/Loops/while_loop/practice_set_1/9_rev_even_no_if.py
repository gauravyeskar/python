print("Reverse Even number without if")
start = int(input("Enter from starting number: "))
end = int(input("Enter to ending number: "))
start+=start%2
i=start
while(i >= end):
    print(i)
    i-=2
