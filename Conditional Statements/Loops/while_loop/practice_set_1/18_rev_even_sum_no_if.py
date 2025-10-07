print("Reverse Even Sum without if")
print("*"*20)
start = int(input("Enter the starting number: ")) #1
end = int(input("Enter the ending number: ")) #10
i=start
sum = 0 
while(end >= i): # 10>=1
    print(end,"+ ",end="")
    sum += end
    end-=2
print("= ",sum)