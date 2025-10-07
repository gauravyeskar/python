s = 'hello@1234'
count = 0
length = 0
sum=0
for i in s:
    if(i>= chr(48) and i<= chr(57)):
        count+=1
for j in s:
    if(j>=chr(48) and j<= chr(57)):
        a=int(j)
        sum+= a
        length+=1
        if(length < count):
            print(a,"+",end = " ")
        else:
            print(a,"= ",sum)
            