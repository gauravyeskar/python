#Even odd even odd pattern (2,1,4,3,6,5,8,7)
n = int(input("Enter the number: "))
i=1
while(i<=n):
    if(i%2==0):
        print(i,",",end=" ")
        if(i<n):
            print(odd,",",end = " ")
        else: 
            print(odd)
    else:
        odd=i
    i+=1
    