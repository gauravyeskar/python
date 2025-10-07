''' 1 
    2 3 
    4 5 6 
    7 8 9 10 
    6 5 4 
    3 2 
    1  '''

n = 4
num= 1
i = 1
while i <= n:
    j = 1
    while j <= i:
        print(num, end=" ")
        num += 1
        j += 1
    print()
    i += 1
num -= 1

n = 3
num = 6
i = 1
while i <= n:
    j = 1
    while j <= (n - i + 1):
        print(num,end= " ")
        num -=1
        j +=1
    print(" ")
    i += 1
