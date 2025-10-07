# Reverse Addition

d = {'a':10,'b':20,'c':30}
d = list(d.values())
s = len(d)
rev = []
for j in range(s-1,-1,-1):
    rev.append(d[j])
count = 0
sum = 0
for j in rev:
    count += 1
    if(count < s):
        sum += j
        print("{} +".format(j),end= " ")
    else:
        sum += j
        print("{} =".format(j),sum)