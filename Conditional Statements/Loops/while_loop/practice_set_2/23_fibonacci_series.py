# Fibonacci series
n = int(input("Enter the number: ")) #7
a,b=0,1
counter = 0
while(counter <= n):
    print(a,end=" ")
    a,b = b,a+b
    counter+=1
