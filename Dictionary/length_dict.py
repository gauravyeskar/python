d = {}
s = int(input("Enter the size: "))
for i in range(s):
    name = input("Enter the name: ")
    value = int(input("Enter the value: "))
    d[name] = value
count = 0
for i in d:
    count+=1
print("*"*20)
print("The length of Dictionary is: ",count)