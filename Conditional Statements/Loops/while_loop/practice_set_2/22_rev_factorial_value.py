num = int(input("Enter the number for factorial: ")) #5
fact = 1 #5,20,60,120
i = num  # 5=5
while( i > 0):  # 5 > 0
    fact = fact * i   # 1 * 5
    if(i > 1): # 5 > 1
        print(i,"*",end=" ") 
    else: 
        print(i,"= ",end = " ") 
    i-=1
print(fact)