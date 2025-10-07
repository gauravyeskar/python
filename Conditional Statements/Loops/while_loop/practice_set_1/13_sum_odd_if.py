print("Sum of odd numbers with if")
start = int(input("Enter the Starting number: "))
end = int(input("Enter the Ending number: "))
i = start
sum=0

while(i <= end):
    if(i % 2 != 0):
        if(i<end):
            print(i,"+ ",end="")
        else:
            sum2=sum+end
            print(i,"= ",sum2)
        sum+=i
    i+=1