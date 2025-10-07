print("Odd number sum without if")
print("*"*20)
start = int(input("Enter the starting number: "))
end = int(input("enter the ending number: ")) #10
i = start #1
sum = 0
while(i <= end):
    print(i,"+ ",end="")
    sum +=i
    i+=2
print("=",sum)