# Even odd
s = int(input("Enter the size: "))
t = ()
even_count = 0
odd_count = 0
even_tup = ()
odd_tup = ()
for i in range(0,s):
    val = int(input("Enter the values: "))
    t = list(t)
    t.append(val)
for j in t:
    if(j%2 == 0):
        print(j," is Even number.")
        even_count += 1
        even_tup = list(even_tup)
        even_tup.append(j)
    else:
        print(j," is Odd number.")
        odd_count +=1
        odd_tup = list(odd_tup)
        odd_tup.append(j)
print("*"*20)
print("Total Even count: ",even_count)
print("Total Even count: ",odd_count)
print("*"*20)
print("Even Tuple",even_tup)
print("Odd Tuple",odd_tup)