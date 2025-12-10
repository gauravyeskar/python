# Biggest and second biggest
'''s = int(input("Enter size of list: "))
lst = []
for i in range(s):
    val = int(input(f"Enter element {i+1}: "))
    lst.append(val)

biggest = second_biggest = float('-inf')

for j in lst:
    if j > biggest:
        second_biggest = biggest
        biggest = j
    elif j > second_biggest and j != biggest:
        second_biggest = j

print("Biggest value:", biggest)
if second_biggest != float('-inf'):
    print("Second biggest value:", second_biggest)
else:
    print("Second biggest value: Not found (all elements are same)")'''

##########################################################################
# 2. 
'''scores = [10,20,100,50,1,80,4,90]
scores.sort()
print(f"Sorted List: {scores}")
second_lowest = scores[1]
second_highest = scores[-2]
print(f"2nd Lowest Value: {second_lowest}")
print(f"2nd Highest Value: {second_highest}")'''

# 3. 
'''dup_scores = [10,20,10,90,20,1,50,1,80,4,90]
unique_Score = list(set(dup_scores))
unique_Score.sort()
print(f"Sorted List: {unique_Score}")
sec_lowest = unique_Score[1]
sec_high = unique_Score[-2]
print(f"2nd Lowest Value: {sec_lowest}")
print(f"Highest Value: {sec_high}")'''