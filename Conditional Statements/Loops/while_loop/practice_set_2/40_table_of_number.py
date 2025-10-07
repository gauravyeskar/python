n = 1634
while(n > 0):
    digit = (n % 10) 
    i = 1
    while(i<=10):
        print(digit, "*" ,i, "= ",digit*i)
        i+=1
        print()
    n//=10