'''   MAP() :- The map() function is used for transformation. always returns a new value for the input object , For every value something will get as an output.
1. The map() will calculate the operation and returns the value in the new list.
2. The map() will check all the elements of the iterable object and returns the result for each of the object.

Syntax:- 
            varname = map(fun_name , iterable_obj)
        
'''
# EXAMPLE 1:-
'''
def square(n):
    return(n**2)
lst = [2,3,4,-2,-3]
mobj = map(square,lst)
print("Original List:- ",lst)
print("Map Object :- ",mobj,type(mobj))
sqlist = list(mobj)
print("Square list :- ",sqlist)
'''

# EXAMPLE 2 :- 
'''
def square(n):
    return(n**2)

print("Enter list of values seperated by space :- ")
lst = [int(val) for val in input().split()]
sqlist = list(map(square,lst))
print("*"*20)
print("Given number Square :- ")
for gn,sn in zip(lst,sqlist):
    print("{} {} ".format(gn,sn))
print("*"*20)
'''

#EXAPMLE :- 3
'''
print("Enter the list of values seperated by spaces :- ")
lst = [int(val) for val in input().split()]
sqlst = list(map(lambda n:n**2,lst))
print("*"*20)
print("The Given Number :- ")
for ln,sn in zip(lst,sqlst):
    print("{}  {} ".format(ln,sn))
print("-"*20)
'''

# EXAMPLE 4 :- 
'''
print("Enter the old salary list seperated by space :- ")
oldsallst = [int(val) for val in input().split() if int (val) > 0]
print("old Salary list :- ",oldsallst)
newsallst = list(map(lambda sal:sal+sal*100/100,oldsallst))
print("*"*20)
print("Old Salary    New Salary")
for osal,nsal in zip(oldsallst,newsallst):
    print("{}    {}".format(osal,nsal))
print("-"*20)
'''

# EXAMPLE 5 :- 
'''
lst1 = [10,20,30,40,50]
lst2 = [100,200,300,400,500]
lst3 = list(map(lambda fv1,fv2:fv1+fv2,lst1,lst2))
print("*"*20)
print("Fv     Sv    Sum")
for fv1,fv2,sv in zip(lst1,lst2,lst3):
    print("{}    {}    {}".format(fv1,fv2,sv))
print("-"*20)
'''

# EXAMPLE 6 :-
print("Enter the elements for list1 seperated by space :- ")
lst1 = [int(val) for val in input().split()]
print("Enter the elements for list2 seperated by space :- ")
lst2 = [int(val) for val in input().split()]
if(len(lst1) > len(lst2)):
    for i in range(1,(len(lst1)-len(lst2))+1):
        lst2.append(0)
elif(len(lst2) > len(lst1)):
    for i in range(1,(len(lst2) - len(lst1))+1):
        lst1.append(0)
lst3 = list(map(lambda fv1,fv2 : fv1 + fv2 , lst1,lst2))
print("*"*20)
print("fv    Sv     Sum")
print("-"*20)
for v1,v2,v3 in zip(lst1,lst2,lst3):
    print("{}     {}    {}".format(v1,v2,v3))
print("-"*20)