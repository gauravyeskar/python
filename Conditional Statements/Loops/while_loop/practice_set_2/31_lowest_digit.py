n = 6340
lowest = 1
while(n>0):
    last_digit = n % 10
    if last_digit < lowest:
        lowest=last_digit
    n//=10
print(f"The lowest digit is {lowest}")