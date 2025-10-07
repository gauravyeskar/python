# Table
s = int(input("Enter the size: "))
l = []
for i in range(0,s):
    val = int(input("Enter the value: "))
    l.append(val)
for i in l:
    ans = 0
    for j in range(1,11):
        ans = i * j 
        print("{} * {} = {}".format(i,j,ans))
    print("*"*30)