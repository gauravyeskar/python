n = 1634
sum = 0
while(n> 0):
    digit = n % 10
    if digit > 1:
        print(digit,"+",end = " ")
    else: 
        print(digit, " = ",end = " ")
    sum = sum + digit
    n//=10
print(sum)