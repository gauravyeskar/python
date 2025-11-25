# For tuple
tpl = (10,"Gaurav",30.34,"India",True,2+3j)
# Converting iterable object into object by using iter(iteraable object).
tpliter = iter(tpl)
print("Type of lst: ",type(tpl)) # <class 'tuple'>
print("Type of lstiter: ",type(tpliter)) # <class 'tuple_iterator'>
print("---------------------------------")
print(tpl)
print(next(tpliter))

while True:
    try:
        print(next(tpliter))
    except:
        print("Value Exceeded.")
        break