s = int(input("Enter the size:- "))
l = []
even_count = 0
odd_count = 0
even_num = []
even_num_count = 0
odd_num = []
odd_num_count = 0
for i in range(s):
    val = int(input("Enter the value: "))
    l.append(val)
for i in l:
    if(i%2==0):
        even_count +=1
        even_num.append(i)
        print("{} is Even number.".format(i))
    else:
        odd_count +=1
        odd_num.append(i)
        print("{} is an Odd number.".format(i))
print("*"*20)
print("Total even numbers are: ",even_num)
print("Total odd numbers are: ",odd_num)
print("*"*20)

even_sum= 0
odd_sum = 0
for e in even_num:
    even_num_count += 1
    if(even_num_count < len(even_num)):
        even_sum += e
        print("{} +".format(e),end=" ")
    else:
        even_sum += e
        print("{} =".format(e),even_sum)
for e in odd_num:
    odd_num_count += 1
    if(odd_num_count < len(odd_num)):
        print("{} +".format(e),end=" ")
    else:
        even_sum += e
        print("{} =".format(e),odd_sum)