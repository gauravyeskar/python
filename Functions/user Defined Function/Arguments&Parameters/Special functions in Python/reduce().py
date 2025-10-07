'''  REDUCE() :-  to run reduce you need to import functools first or error will occur.
1. The Python function reduce() is part of the functools module. 
2. The reduce() is used for obtaining a single element result from given iterable object by applying to a function.
3. how it works it initially selects 2 values of the iterable object and place them un first and second variable. 
    when the values are given to a specified condition in lambda or normal function it is calculating and
    for the next iteration it will take only one input instead of three inputs. 

    eg:- 10    20    30    40    50
         x   +  y    (10+20=30) 
                x  +  y  (30+30=60)
                      x +  y (60+40=100)
                           x   +  y (100+50)
                                      output = 150

'''
import functools
'''def add(x,y):
    return(x+y)
res = functools.reduce(add,(10,20))
print(res)
'''

# EXAMPLE 1 :- 
'''def sum(a,b):
    return(a+b)
print("Enter the list of values seperated by space :-")
lst = [int(val) for val in input().split()]
res = functools.reduce(sum,lst)
print("Sum = ",res)
'''

# EXAMPLE 2 :- For accepting the list of values and find min and max by reduce().
'''
print("Enter the list of values seperated by spaces :- ")
lst = [int(val) for val in input().split()]
max = functools.reduce(lambda f,s:f > s ,lst)
min = functools.reduce(lambda f,s:f < s ,lst)
print("Max({}) = {}".format(lst,max))
print("Min({}) = {}".format(lst,min))
'''

# EXAMPLE 3 :- Acceptong the list of words and join them using reduce().
'''
print("Enter list of words seperated by comma's :- ")
lst = [val for val in input().split()]
print("Given Words = ",lst)
line = functools.reduce(lambda x,y :x+' ' +y,lst).upper()
print("Line = ",line)
'''