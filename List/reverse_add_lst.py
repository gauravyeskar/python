# Reverse addition
s = int(input("Enter the size: "))
lst = []
rev = []
count = 0
sum = 0
for i in range(0,s):
    val = int(input("Enter the value: "))
    lst.append(val)
for j in range(s-1,-1,-1):
    rev.append(lst[j])
for i in rev:
    count += 1
    if(count<s):
        sum += i
        print("{} +".format(i),end=" ")
    else:
        sum +=i
        print("{} = ".format(i),sum)
