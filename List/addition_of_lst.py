# Addition of list
a = int(input("Enter the size :"))
l=[]
for k in range(0,a):
    val= int(input("Enter the value :"))
    l.append(val)
sum = 0
count = 0
length = 0
for i in l:
    count +=1
for j in l:
    sum +=j
    length += 1
    if(length < count):
        print('{} + '.format(j),end= "")
    else:
        print('{} = '.format(j),sum)