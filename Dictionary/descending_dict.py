# Descending dict.
d = {}
s = int(input("Enter the size: "))
for i in range(s):
    name = input("Enter the key name: ")
    value = int(input("Enter the key value: "))
    d[name] = value
# l = sorted(d.values(),reverse=True)
l = list(d.values())
for j in range(s):
    for k in range(s-1):
        if(l[k]<l[k+1]):
            l[k],l[k+1] = l[k+1],l[k]
print("The values in Descending are",l)