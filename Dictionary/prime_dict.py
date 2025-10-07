d = {}
s = int(input("Enter the size: "))
for i in range(s):
    key = input("Enter the key name: ")
    val = int(input("Enter the value: "))
    d[key] = val
for i in d:
    val = d[i]
if val > 0:
    is_prime=True
    for j in range(2,val):
        if(val%j == 0):
            is_prime = False
            break
    if is_prime:
        print("{} is prime number.".format(val))
    else:
        print("{} is not prime number.".format(val))
else:
    print("{} is not prime number.".format(val))