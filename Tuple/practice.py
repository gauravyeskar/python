#TUPLE:
'''
1. represented by '(  )'
2. Immutable
3. Stores group of value of same type or different datatype.
4. Similar to list but tuple is read-only we cannot modify elements inside tuple.
5. It occupies less memory space compared to list.
6. If we have to modify tuple we have to convert it into list and we have to modify it and then again convert it to tuple.
'''
t = (10,20,30)
print(t,type(t))

#converting a tuple in list and then to tuple again
l = list(t)
print(l,type(l))

l.append(10)

t = tuple(l)
print(t,type(t))