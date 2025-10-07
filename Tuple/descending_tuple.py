# Descending Tuple
s = int(input("Enter the size:- "))
t = []
for i in range(s):
    val = int(input("Enter the value:- "))
    t.append(val)
for j in range(0,s):
    for k in range(j+1,s):
        if(t[j]<t[k]):
            t[j],t[k] = t[k],t[j]
t = tuple(t)
print("Descending Tuple is: ",t)