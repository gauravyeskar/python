num = int(input("Enter the number: "))
i = 2
not_prime=0
if(num <=1):
    if(num ==0):
        print(num,"is neutral.")
    elif(num<0):
        print(num,'is negative.')
    else:
        print(num,"is a prime.")
else:
    while(i<=num-1):
        if(num%i==0):
            not_prime=1
        i+=1
    if(not_prime>=1):
        print(num,"is not prime number")
    else:
        print(num,"is a prime number.")