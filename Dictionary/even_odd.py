# Even odd Dictionary

d = {}
s = int(input("Enter the size: "))
for i in range(s):
    name = input("Enter the key name: ")
    value = int(input("Enter the key value: "))
    print("*"*20)
    d[name] = value
d.values()
even = 0
even_dict = []
odd = 0
odd_dict = []
for j in d.values():
    if(j%2==0):
        even +=1
        even_dict.append(j)
        print("{} is even number.".format(j))
    else:
        odd +=1
        odd_dict.append(j)
        print("{} is odd number.".format(j))
print("*"*20)
print("Even count is: ",even)
print("Even numbers are: ",even_dict)
print("Odd count is: ",odd)
print("Odd numbers are: ",odd_dict)
print("*"*20)