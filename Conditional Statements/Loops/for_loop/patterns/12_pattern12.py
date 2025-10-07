''' 1 
    2 3 
    4 5 6 
    7 8 9 10 
    6 5 4 
    3 2 
    1  '''

row  = 4
start = 1
for i in range(1,row+1,1):
    for j in range(i):
        print(start,end = " ")
        start+=1
    print()

row1 = 3
endd = 6
for k in range(row1,0,-1):
    for l in range(k):
        print(endd , end= " ")
        endd -= 1
    print()
