# 1.
'''numbers = [10, 25, 3, 40, 12, 7, 50]
min_val = numbers[0]
max_val = numbers[0]

for num in numbers[1:]:
    if num < min_val:
        min_val = num
    if num > max_val:
        max_val = num
print(f"Lowest Value: {min_val}")
print(f"Highest Value: {max_val}")'''

# 2.
'''numbers = [10, 25, 3, 40, 12, 7, 50]
numbers.sort()
print(f"Lowest Value: {numbers[0]}")
print(f"Highest Value: {numbers[-1]}")'''

# 3.
print(f"Lowest Value: {min(10,20,90,50,1,80,4,90)}")
print(f"Hightest Value: {max(10,20,90,50,1,80,4,90)}")