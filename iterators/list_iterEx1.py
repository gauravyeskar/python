# For list
lst = [10,20,30,40,50,60,70,80]
# Converting iterable object into object by using iter(iteraable object).
lstiter = iter(lst)
print("Type of lst: ",type(lst)) # <class 'list'>
print("Type of lstiter: ",type(lstiter)) # <class 'list_iterator'>
print("---------------------------------")
print(next(lstiter))
print(next(lstiter))

while True:
    try:
        print(next(lstiter))
    except:
        print("Value Exceeded.")
        break