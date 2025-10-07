# list number length
s = int(input("Enter the size: "))
L = []
for i in range(s):
    val = int(input("Enter the value: "))
    L.append(val)
print(L)
for i in L:
    t = i
    length = 0
    while(i>0):
        length +=1
        t //= 10
    print(f"Number {i} has {length} digits")