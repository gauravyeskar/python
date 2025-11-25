'''# For dict
dict = {10:"Gaurav",30:'D Sc',20:"India",40:'C++',50:"C"}
# Converting iterable object into object by using iter(iteraable object).
dictiter = iter(dict)
print("Type of lst: ",type(dict)) # <class 'dict'>
print("Type of lstiter: ",type(dictiter)) # <class 'dict_keyiterator'>
print("---------------------------------")
print(dict)
print(next(dictiter))

while True:
    try:
        print(next(dictiter)) # Will return only keys.
    except:
        print("Value Exceeded.")
        break'''

# ######################################################################
# for loop
# For dict
dict = {10:"Gaurav",30:'D Sc',20:"India",40:'C++',50:"C"}
# Converting iterable object into object by using iter(iteraable object).
dictiter = iter(dict)
print("Type of lst: ",type(dict)) # <class 'dict'>
print("Type of lstiter: ",type(dictiter)) # <class 'dict_keyiterator'>
print("---------------------------------")
# for k in dictiter:
#     print(k)
print("------------------------------------")
for k in dictiter:
    print("{} ---> {}".format(k,dict.get(k)))
print("------------------------------------")
