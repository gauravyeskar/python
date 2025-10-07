print("Sum of reverse Odd numbers")
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
i=start
sum=0
while(i>=end and i%2!=0):
    if(i>end):
        print(i,"+",end="")
    else: 
        sum2=sum+end
        print(i,"=",sum2,end="")
    sum+=i
    i-=2