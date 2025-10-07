n = 1634
sum = 0
while(n > 0):
    digit = n %  10
    if digit % 2 !=0:
        sum = sum + digit
    n //=10
print(f"The sum of Odd numbers is {sum}")