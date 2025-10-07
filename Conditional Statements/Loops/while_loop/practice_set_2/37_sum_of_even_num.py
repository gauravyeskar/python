n = 1234
even_sum = 0
while(n > 0):
    digit = n % 10
    if(digit % 2 == 0):
        even_sum = even_sum + digit
    n//=10
print(f"Sum of Even numbers is {even_sum}")