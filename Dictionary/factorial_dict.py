# Factorial Dict
d = {}
s = int(input("Enter the size: "))
for i in range(s):
    key = input("Enter the key name: ")
    value = int(input("Enter the value: "))
    d[key] = value
result = {}
for key in d:
    value = d[key]
    fact = 1
    for i in range(1, value + 1):
        fact = fact * i
    result[key] = fact
print("*"*20)
print("Original Dictionary: ",d)
print("Factorial dictionary: ", result)