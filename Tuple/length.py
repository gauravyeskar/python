#Length Tuple
s = int(input("Enter the size: "))
t = ()
count = 0
for i in range(0,s):
    val = int(input("enter the value: "))
    count += 1
    t = list(t)
    t.append(val)
t = tuple(t)
print("*"*20)
print(t,type(t))
print("Count is: ",count)