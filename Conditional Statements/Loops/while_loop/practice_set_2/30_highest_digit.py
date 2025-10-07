n = 1634
highest = 0

while n > 0:
    digit = n % 10       
    if digit > highest:  
        highest = digit
    n //= 10            

print("Highest digit is:", highest)