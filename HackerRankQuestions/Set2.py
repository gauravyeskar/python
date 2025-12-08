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
from collections import Counter
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
    solve_company_logo(s)

