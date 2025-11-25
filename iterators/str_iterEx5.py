# For string
s = 'PYTHON'
# Converting iterable object by using iter(iterable object)
siter = iter(s)
print('Type of s: ',type(s)) #<class 'str'>
print("Type of siter: ",type(siter)) # <class 'str_ascii_iterator'>
for i in siter:
    print(i)