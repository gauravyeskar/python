# Ascending order

d = {}
s = int(input("Enter the size: "))
for k in range(s):
    name = input("Enter the key name value: ")
    value = int(input("Enter the key value: "))
    d[name] = value
list = list(d.values())
for i in range(0,s):
    for j in range(0,s-1):
        if(list[j]>list[j+1]):
            list[j],list[j+1] = list[j+1],list[j]
print(list)