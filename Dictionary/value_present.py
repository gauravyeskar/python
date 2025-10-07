d = {}
s = int(input("Enter the size: "))
for i in range(s):
    name = input("Enter the key name: ")
    value = int(input("Enter the value: "))
    d[name] = value

key_name = input("enter the key_name: ")

if key_name in d:
    print({key_name}, "key name is available")
else:
    print({key_name}, "key name is not available")