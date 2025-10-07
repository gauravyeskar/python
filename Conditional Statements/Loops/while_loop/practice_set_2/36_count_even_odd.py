n = 16459
even_count= 0
odd_count = 0
while(n > 0):
    digit = n % 10
    if(digit % 2 == 0):
        even_count+=1
    else:
        odd_count+=1
    n//=10
print(f"The Even count is {even_count}")
print(f"The odd count is {odd_count}")