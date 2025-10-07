''' A 
    B B 
    C C C 
    D D D D 
    E E E E E   '''

for i in range(1,6,1):
    for j in range(1,i+1,1):
        print(chr(64+i),end= " ")
    print()