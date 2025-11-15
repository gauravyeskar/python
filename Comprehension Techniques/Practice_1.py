# Squaring List Elements: Create a new list containing the square of every integer in the input list.
'''numbers = [1, 2, 3, 4, 5]
op = [i*i for i in numbers]
print(op)'''

# Uppercase Conversion: Convert every string in the list to uppercase.	
'''words = ['hello', 'python', 'comp']
op = [i.upper() for i in words]
print(op)'''

# Filter Even Numbers: Create a new list containing only the even numbers from the original list.	
'''data = [1, 2, 9, 12, 15, 20]
op = [i for i in data if i%2==0]
print(op)'''

# Filter Long Strings: Filter the list to include only strings that have a length strictly greater than 5 characters.	
'''names = ['Anna', 'Brenda', 'Chris', 'David']
op = [i for i in names if len(i)>5]
print(op)'''

# Map & Filter (Square Evens): Square the numbers, but only if the original number is even.	
'''data = [1, 2, 3, 4, 5, 6]
op = [i for i in data if i%2==0]
print(op)'''

# Initials Filter: Get the first character (initial) of every name that starts with 'A'.	
'''names = ['Adam', 'Brian', 'Alice', 'Charlie']
op = [j for i in names for j in i if j=='A']
print(op)'''

# Float to Int: Convert all floating-point numbers in the list to integers.	
'''floats = [1.5, 2.7, 3.0, 4.2]
print([int(i) for i in floats])'''

# Positive/Zero Replacement (Ternary): Replace all negative numbers with 0, but keep all positive numbers as they are.	
'''values = [10, -5, 8, -20, 15]
op = [ i if i>=0 else 0 for i in values ]
print(op)'''

# Number Classification: Classify each number as 'Small' (if $\le 10$) or 'Large' (if $> 10$).
'''nums = [5, 12, 10, 25, 1]
op = ['Small' if i<= 10 else 'Large' for i in nums ]
print(op)'''

# Length Label: If a string's length is even, append " (Even)", otherwise append " (Odd)".
'''words = ['cat', 'dog', 'house', 'car']
op = [i + ' (Even)' if len(i)%2==0 else i + ' (Odd)' for i in words ]
print(op)'''

# Default Value (Ternary): If a value is None, replace it with the string "N/A"; otherwise, use the value itself.	
'''data = [1, 'text', None, 42, None]
op = ['NA' if i== None else i for i in data ]
print(op)'''

# Grade Status (Ternary): Convert numeric grades to 'Pass' (if $\ge 60$) or 'Fail' (if $< 60$).
'''grades = [75, 55, 90, 45, 60]
op = ['Pass' if i>=60 else 'Fail' for i in grades]
print(op)'''

# Flatten 2D List (Nested): Flatten a simple list of lists (a 2D matrix) into a single 1D list.	
'''matrix = [[1, 2], [3, 4], [5, 6]]
op = [ j for i in matrix for j in i ]
print(op)'''

# Matrix Transposition (Nested): Transpose a given square matrix (swap rows and columns) using a single list comprehension.	
'''matrix = [[1, 2], [3, 4]]
num_rows = len(matrix)
num_cols = len(matrix[0])
op = [[matrix[r][c] for r in range(num_rows)] for c in range(num_cols)]
print(op)'''

#Filter Unique Pairs (Nested): Generate a list of all coordinate pairs $(x, y)$ where $x$ is from list $X$ and $y$ is from list $Y$, and $x \neq y$.
'''X = [1, 2]
Y = [1, 3]
op = [ (x,y) for x in X for y in Y if x!=y]
print(op)'''

# Cartesian Product (Modulus Filter): Generate the product of two lists (all pairs), 
# but only include pairs where the sum of the elements is divisible by 3.	
'''L1 = [1, 2]
L2 = [3, 4]
op = [ (x,y) for x in L1 for y in L2 if (x+y)%3==0 ]
print(op)'''

# Set Comprehension: Use a set comprehension to find the unique lengths of the words in the list.	
'''text = ['a', 'cat', 'is', 'a', 'pet']
op = { len(i) for i in text} 
print(op)'''

# Dictionary Comprehension (Swap): Create a dictionary comprehension that swaps the keys and values of the input dictionary. (Assume all values are unique).
d = {'a': 1, 'b': 2, 'c': 3}
op = {x:y for x,y in d.items()}
print(op)