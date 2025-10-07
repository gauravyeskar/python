print("Even number sum without if")
start = int(input("Enter the Even starting number: "))
end = int(input("Enter the ending number: "))
i = start
sum = 0
while(i <= end):
    print(i,"+ ",end="")
    sum = sum+i
    i+=2
print("= ",sum)