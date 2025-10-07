print("Reverse Odd number without if")
start = int(input("Enter the starting number: ")) #1
end = int(input("Enter the ending number: "))# 10
i = end
sum = 0
while(i >= start ):
    print(i,"+ ",end="")
    sum+=i
    i-=2
print(" =",sum)