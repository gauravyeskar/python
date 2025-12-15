# 1. 
'''Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function
that multiplies argument x with argument y and prints the result.  
Sample Output:25      48'''
'''y = lambda x:x+15
print(y(10))
r = lambda x,y:x*y
print(r(12,4))'''

# 2.
'''Write a Python program to create a function that takes one argument, and that argument 
will be multiplied with an unknown given number.'''
'''def gen(n):
    return lambda x:x*n
res = gen(2)
print("Result:- ",res(15))'''

# 3.
'''Write a Python program to sort a list of tuples using Lambda.
Original list of tuples:  [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]'''
'''subs = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
subs.sort(key=lambda x:x[1])
print(subs)'''

# 4. 
'''Write a Python program to sort a list of dictionaries using Lambda.
Original list of dictionaries : [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]'''
dictonary = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
