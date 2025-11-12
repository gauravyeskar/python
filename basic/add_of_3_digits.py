num = int(input("Enter the number value: "))
a = num // 100
b = (num // 10) % 10
c = num % 10
d = a+b+c
print(a)
print(b)
print(c)
print("The sum of the digits is: ",d)