# length
s = int(input("Enter the size: "))
l= []
count = 0
for i in range(s):
    val = int(input("Enter the value: "))
    l.append(val)
    count +=1
print("The total count is: ",count)