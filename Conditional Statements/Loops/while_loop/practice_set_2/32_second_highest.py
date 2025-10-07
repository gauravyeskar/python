n = 1234
highest = 0
second_highest = 0
while(n>0):
    ld = (n // 10) % 10
    if ld > second_highest:
       second_highest = ld
    n//=10
print(second_highest)
