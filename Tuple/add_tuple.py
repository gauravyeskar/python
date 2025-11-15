#ADDITION OF TUPLE ELEMENTS

s = int(input("Enter the size: "))
t = ()
sum = 0
count = 0
for i in range(0,s):
    val = int(input("Enter the values: "))
    t = list(t)
    t.append(val)
t = tuple(t)
for j in t:
    count += 1
    sum += j
    if count < s:
        print("{} + ".format(j),end = " ")
    else:
        print("{} = ".format(j),end= " ")
print(sum)
print(t,type(t))
print("-"*20)