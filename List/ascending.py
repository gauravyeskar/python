#  Ascending list
s = int(input("Enter the size:- "))
l = []
for i in range(s):
    val =int(input("Enter the value: "))
    l.append(val)
for j in range(0,s):
    for k in range(j+1,s):
        if(l[j]> l[k]):
            l[j],l[k] = l[k],l[j]
print("Ascending list is: ",l)