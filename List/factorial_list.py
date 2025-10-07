s = int(input("Enter the size: "))
l = []
result = []

for i in range(s):
    val = int(input("Enter the value: "))
    l.append(val)

for i in l:
    fact = 1
    for j in range(1, i + 1):
        fact = fact * j
    result.append(fact)

print("Factorials are:", result)