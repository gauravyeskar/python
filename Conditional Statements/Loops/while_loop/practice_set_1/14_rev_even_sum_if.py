print("Sum of Even numbers with if")
start=int(input("Enter the start number: "))
end=int(input("Enter the end number: "))
print("*"*40)
i=start
sum=0
while(i<=end):
    if(i%2==0):
        if(i<end):
            print(i,"+ ",end="")
        else:
            sum2 = sum+end
            print(i,"= ",sum2)
        sum+=i        
    i+=1