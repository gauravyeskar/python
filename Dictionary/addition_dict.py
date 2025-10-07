# Dictionary addition.

d = {}
s = int(input("Enter the size: "))
for i in range(s):
    key_name = input("Enter the key name: ")
    key_value = int(input("Enter the key value: "))
    print("*"*20)
    d[key_name] = key_value
count = 0
sum = 0
d1 = d.values()
for i in d1:
    count += 1
    sum += i
    if(count < s):
        print("{} +".format(i),end = " ")
    else:
        print("{} =".format(i),sum)
        print("*"*20)