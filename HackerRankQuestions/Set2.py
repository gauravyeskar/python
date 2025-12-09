'''
Given an integer,n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird  '''

'''n = int(input("Enter the num: ").strip())
if (n%2 != 0):
    print("Weird")   
else:
    if(n>=2 and n<=5):
        print("Not Weird")
    elif(n>=6 and n<=20):
        print("Weird")
    elif(n>=20):
        print("Not Weird")'''

###############################################################################################.
'''
if the cubes are 4 3 2 1 3 4: 
    You can pick 4 from the right (Stack: [4], Remaining: 4 3 2 1 3).Next, both ends have 4 and 3. The top of stack is 4. 
    You must pick one <=4. You pick 4 from the left. (Stack: [4, 4], Remaining: 3 2 1 3).Next, ends are 3 and 3. 
    Top is 4. Pick one. (Stack: [4, 4, 3], Remaining: 2 1 3).Next, ends are 2 and 3. Top is 3. Pick one <=3.
    You pick 3 from the right. (Stack: [4, 4, 3, 3], Remaining: 2 1).Next, ends are 2 and 1. Top is 3. Pick one <=3. 
    You pick 2 from the left. (Stack: [4, 4, 3, 3, 2], Remaining: 1).Next, end is 1. Top is 2. Pick 1. (Stack: [4, 4, 3, 3, 2, 1], 
    Remaining: []).This one is possible.
 '''
'''from collections import deque
def can_stack_cubes_corrected(blocks):
    # Use a deque for efficient popping from both ends
    d = deque(blocks)
    # Initialize the top block to a value larger than any possible cube size
    current_top = 2**31 
    
    while d:
        left_val = d[0]
        right_val = d[-1]
        
        # Prioritize picking the larger available cube if both are valid
        if right_val <= current_top and left_val <= current_top:
            if right_val >= left_val:
                current_top = d.pop()
            else:
                current_top = d.popleft()
        elif right_val <= current_top:
            current_top = d.pop()
        elif left_val <= current_top:
            current_top = d.popleft()
        else:
            # If neither the leftmost nor rightmost cube can be placed, return 'No'
            return "No"
            
    # If all cubes are stacked successfully, return 'Yes'
    return "Yes"

# Function to handle the multi-test case input format
def process_test_cases_corrected():
    try:
        # Read the number of test cases
        T = int(input()) 
        for _ in range(T):
            # Read the number of cubes (n) and the side lengths
            n = int(input()) 
            side_lengths = list(map(int, input().split())) 
            # Print only "Yes" or "No" as the output for each case
            print(can_stack_cubes_corrected(side_lengths))
    except EOFError:
        pass
    except ValueError:
        pass

# Call the function to run the solution with standard input
process_test_cases_corrected()
'''

##################################################################################################################
'''
The question asks you to process a single input string and identify the three most common characters within it.
1. Print the three most common characters along with their occurrence count.
2. Sort in descending order of occurrence count.
3. If the occurrence count is the same, sort the characters in alphabetical order.
Eg:- GOOGLE --> G,O,E
'''
'''from collections import Counter
def solve_company_logo(s):
    # 1. Count character occurrences:
    # Counter creates a dictionary-like object: {'a': 2, 'b': 3, 'c': 2, 'd': 1, 'e': 1}
    counts = Counter(s)
    # 2. Sort the items (character, count) pairs:
    # The sorting key is a TUPLE: (-count, character)
    # The minus sign on the count sorts in descending order (highest count first).
    # The character itself sorts alphabetically (for tie-breaking).
    # Example for 'aabbbccde': [('b', 3), ('a', 2), ('c', 2), ('d', 1), ('e', 1)] 
    sorted_items = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    # 3. Print the top three most common characters
    for i in range(3):
        character, count = sorted_items[i]
        # The output format required is "char count"
        print(f"{character} {count}")
# This part handles the input format specified in the problem:
if __name__ == '__main__':
    # Read the single line of input string S
    s = input().strip()
    
    # Run the solution function
    solve_company_logo(s)'''

#####################################################################################################################################
# When see capital letter then it increments and first 3 letters should be lowercase
# I/P:- saveChangesInTheEditor
# O/P:- 5
import math
import os
import random
import re
import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

'''def camelcase(s):
    count = 1
    for i in s:
        if i.isupper():
            count+=1
    return count

s = input("Enter the string:- ")
print(camelcase(s))'''

#######################################################
# Strong Password.
'''
1. Its length is atleast 6
2. It contains at least one digit.
3. It contians at least one lowercase English character.
4. It contains atleast one uppercase.
5. It contains atleast one special characters.'''
'''n = int(input("Enter the num:- "))
paswrd = input("Enter the Pass:- ")
has_digit = False
has_lower = False
has_upper = False
has_special = False
for i in paswrd:
    if len(i)>=6:
        if i.isupper():
            has_upper = True
        elif i.islower():
            has_lower = True
        elif i.isdigit():
            has_digit = True
        elif i in ('!@#$%^&*()-+ '):
            has_special = True
miss_count = 0
if not has_digit:
    miss_count +=1
if not has_lower:
    miss_count +=1
if not has_upper:
    miss_count +=1
if not has_special:
    miss_count  +=1
chars_needed = max(0,6-n)
print(max(miss_count,chars_needed))'''

#################################################################################
'''
The "Alternate" problem asks you to find the longest possible substring that meets two conditions:
It must be composed of exactly two unique, strictly alternating characters (e.g. bebebe).
To form this substring, you can only remove characters from the original string by deleting all instances of a specific character type.
The goal is to test all possible pairs of characters, find the length of the longest valid resulting string, or return 0 if none can be formed.
'''
'''import math
import os
import random
import re
import sys
from itertools import combinations

def alternate(s):
    unique_chars = set(s)
    max_len = 0
    
    for i,j in combinations(unique_chars,2):
        temp_string = "".join([c for c in s if c in(i,j)])

        is_valid = True
        for i in range(1,len(temp_string)):
            if temp_string[i] == temp_string[i-1]:
                is_valid = False
                break
        
        if is_valid:
            max_len = max(max_len,len(temp_string))
    return max_len
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    l = int(input().strip())
    s = input()'''
#########################################################################