# Input: arr[] = [54, 43, 2, 1, 5]
# Output: 54 43 2 1 5
'''def list_traversal(lst):
    for i in lst:
        print(i,end=" ")

list_traversal([54,10,60,80,20])'''

# Length of list
'''def lst_len(lst):
    count = 0
    for i in lst:
        count +=1
    print(count)
lst_len([54,10,60,80,20])'''

# Sum of List
'''def list_sum(lst):
    Total_count = 0
    for i in lst:
        Total_count += 1
    sum = 0
    count = 0
    for i in lst:
        count += 1
        if count < Total_count:
            print(i,end="+ ")
            sum += i
        else:
            sum += i
            print(i,end="= ")
            
    print(sum)
list_sum([54,10,60,80,20])'''

