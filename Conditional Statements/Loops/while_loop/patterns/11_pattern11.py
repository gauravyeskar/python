''' 10 9 8 7 
    6 5 4 
    3 2
    1 '''

n = 4
num = 10
i = 1
while i <= n:
    j = 1
    while j <= (n - i + 1):
        print(num,end= " ")
        num -=1
        j +=1
    print(" ")
    i += 1

    