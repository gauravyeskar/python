'''def genrange(val):
    i = 0
    while(i<val):
        return i
        i = i + 1
    
g = genrange(10)
print(type(g)) # here the type of 'g' is "INT" bcz of 'return' keyword.'''

def genrange(val):
    i = 0
    while(i<val):
        yield i
        i = i + 1
    
g = genrange(4)
#print(type(g)) # here the type of 'g' is "GENERATOR" bcz of 'yield' keyword.
print(next(g)) # It gives the next value from the generator
print(next(g)) # The many times u call the next value will be called.
print(next(g)) 
print(next(g))
print(next(g)) # This generates the StopIteration error becz of the value exceeded. 
