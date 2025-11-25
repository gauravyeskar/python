def genrange(val):
    i = 0
    while(i<val):
        yield i
        i = i + 1
    
g = genrange(4)
#print(type(g)) # here the type of 'g' is "GENERATOR" bcz of 'yield' keyword.
while True:
    try:
        print(next(g)) # This will provide all the values at once.
    except StopIteration:
        print("Value Exceeded.")
        break