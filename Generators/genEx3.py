'''def getcourses():
    yield 'Python'
    yield 'Java'
    yield 'DSA'
    yield 'D Sc'

crs = getcourses()
print(type(crs)) # Its type is 'generators'
print(next(crs)) 
print(next(crs)) '''


############################################################
# Printing by return.
def getcourses():
    return 'Python'
    return 'Java'
    return 'DSA'
    return 'D Sc'

crs = getcourses()
print(type(crs)) # Its type is 'str'
print((crs)) 
print(crs) 
print((crs))  

# But this 3 print statements will provide the same python as an output everytime.
