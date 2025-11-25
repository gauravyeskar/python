# For set
sets = {10,"Gaurav",30.34,"India",True,2+3j,10}
# Converting iterable object into object by using iter(iteraable object).
setiter = iter(sets)
print("Type of lst: ",type(sets)) # <class 'set'>
print("Type of lstiter: ",type(setiter)) # <class 'set_iterator'>
print("---------------------------------") 
print(sets)
print(next(setiter))

while True:
    try:
        print(next(setiter))
    except:
        print("Value Exceeded.")
        break