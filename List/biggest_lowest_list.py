# Biggest and second biggest
s = int(input("Enter size of list: "))
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
    print("Second biggest value: Not found (all elements are same)")