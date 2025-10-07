n = 1234
second_lowest = 10
while(n>0):
    digit= n%10
    if(digit < second_lowest):
        second_lowest= digit
    n//=10
print(second_lowest).