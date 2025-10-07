s = int(input("Enter the size: "))
lst = []
even_count = 0
even = []
odd_count = 0
odd = []
for i in range(s):
    val = int(input("Enter the value: "))
    lst.append(val)
print("Total List is: ",lst)
for j in lst:
    if(j%2==0):
        print("{} is even.".format(j))
        even_count +=1
        even.append(j)
    else:
        print("{} is odd.".format(j))
        odd_count +=1
        odd.append(j)
print("*"*40)
print("Even count is: ",even_count)
print("Even list is: ",even)
print("*"*40)
print("Odd Count is: ",odd_count)
print("odd List is: ",odd)
print("*"*40)