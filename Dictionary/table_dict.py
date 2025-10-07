d = {}
s = int(input("Enter the size: "))
for i in range(s):
    key = input("Enter the key name: ")
    val = int(input("Enter the value: "))
    d[key] = val
print("*"*10)
for k in d:
    value = d[k]
    for j in range(1,11):
        print("{} * {} = {}".format(value,j,value*j))
    print("*"*10)
