s = input("Enter the string: ")
leng = 0
even_count = 0
odd_count = 0
sum_even = 0
sum_odd = 0
for j in s:
    if (j>=chr(48) and j<=chr(57)):
        leng +=1
        even_num = int(j)
        odd_num = int(j)
        if(even_num % 2 == 0):
            even_count +=1
            sum_even+=even_num
        else:  
            odd_count+=1
            odd_num = int(j)
            sum_odd+=odd_num
print("*"*20)
print("Sum of even number is: ",sum_even)
print("Sum of odd number is: ",sum_odd)
print("*"*20)
print("Total count is: ",even_count)
print("Total count is: ",odd_count) 
print("*"*20)