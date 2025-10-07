n = 1634
while n > 0:
    digit = n % 10   
    if digit % 2 == 0:
        print(f"{digit} is Even number.")
    else:
        print(f"{digit} is Odd number.")
    n //= 10  