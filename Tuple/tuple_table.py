#Table Tuple
s = int(input("Enter the size: "))
t =()
for i in range(0,s):
    val = int(input("Enter the value: "))
    t = list(t)
    t.append(val)
for j in t:
    for k in range(1,11):
        print("{} * {} = {}".format(j,k,j*k))
    print("*"*20)
t = tuple(t)
print(t,type(t))