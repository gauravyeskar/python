'''  FILTER():-  The filter() function is used for selection. ,Must return a boolean (True or False) , output will always an original value.
1. it is used for filtering out some elements from list of elements by applying to function.
2. It will check every single element of the iterable object and filter it.
3. Syntax:- 
            varname = filter(fun_nm , iterable_obj{list,tuple,set,dict,or any.}) 
'''

# EXAMPLE 1 :- 
def pos(n):
    if n>0:
        return True
    else:
        return False
'''    
lst = [100,-200,300,-150,-160,230,400,-500]
obj = filter(pos,lst)
print("*"*20)
print("Type of object = ",type(obj))
print("Content of object = ",obj)
pslist = list(obj)
print("Given elements are: ",lst)
print("positive Elements are: ",pslist)
print("*"*20) '''

# EXAMPLE 2:- Without making a function we can run the program by creating the lambda function but it will work only for the specified block.
'''pos = lambda n:n>0
lst = [100,-200,300,-150,-160,230,400,-500]
obj = filter(pos,lst)
print("*"*20)
print("Type of object = ",type(obj))
print("Content of object = ",obj)
pslist = list(obj)
print("Given elements are: ",lst)
print("positive Elements are: ",pslist)
print("*"*20) 
'''

# EXAMPLE 3 :- 
'''
print("Enter the list of values seperated by spaces: ")
lst = [int(val) for val in input().split()]
pslist = list(filter(lambda v:v>0,lst))
nslist  = list(filter(lambda v:v<0,lst))
print("Given elements :- ",lst)
print("Positive Elements :- ",pslist)
print("Negative Elements :- ",nslist)  '''

# EXAMPLE 4 :- 
'''
print("Enter list of value seperated buy space: ")
lst = [int(val) for val in input().split()]
print("Given list = ",lst)
# For even and odd filter:
even_lst= list(filter(lambda i: i%2 == 0,lst))
odd_lst = list(filter(lambda j: j%2 != 0,lst))
print("*"*20)
print("Even list :- ",even_lst)
print("Odd list :- ",odd_lst)
print("*"*20)
'''

# EXAMPLE 5 :-
'''
print("Enter the list of elements seperated by spaces: ")
lst = [int(val) for val in input().split() if int(val) > 0]
print("Given list of elements :- ",lst)
# For even and odd filter:
even_lst= list(filter(lambda i: i%2 == 0,lst))
odd_lst = list(filter(lambda j: j%2 != 0,lst))
print("*"*20)
print("Even list :- ",even_lst)
print("Odd list :- ",odd_lst)
print("*"*20)
'''

# EXAMPLE 6 :-
'''
print("Enter the list of words seperated by comma's :- ")
words = [val for val in input().split(',')]
print("Given words are :- ",words)
wlst = list(filter(lambda w:3<len(w) <= 5,words))
print("Words whose length lies within 3 and 5 are :-",wlst)
'''

# EXAMPLE 7 :-
line = input("Enter the line of text:- ")
print("*"*50)
print("Given line :- ",line)
vlist = list[filter(lambda ch:ch.lower() in ['a','e','i','o','u','A','E','I','O','U'],line)]
clist = list(filter( lambda c:c.isalpha()&c.islower() not in['a'],line))
digit = tuple(filter(lambda d:d.isdigit(),line))
spl_symbl = tuple(filter(lambda ss:(not ss.isalpha()) and (not ss.isdigit()),line))

print("*"*20)
print("Vowels : ",vlist)
print("Consonants :",clist)
print("Digits : ",digit)
print("Special Symbol : ",spl_symbl)
print("-"*50)