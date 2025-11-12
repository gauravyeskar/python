# decorators :- khud bhi ek fuction hai, lega bhi ek function, andhar calayega thi ek function, return bhi karega ek function.

# 1.
'''
def dec(x):
    def inner():
        print("Decoration started..")
        x()
        print("Decoration Ended..!!")
    return inner
 
def code():
    print("PYTHON")

def cpp():
    print("CPP")

a = dec(code)
print(a())
'''
# 2. 
'''def dec(x):
    def inner():
        print("Execution Started...")
        x()
        print("Execution Ended...!!")
    return inner

def add():
    a = int(input("Enter the value 1st:- "))
    b = int(input("Enter the value 2nd:- "))
    c = a+b
    print("The Sum is:- ",c)

def sub(a,b):
    if a > b:
        print("The Substraction is:- ",a-b)
    else:
        print("The Substraction is:- ",b-a)

# z = dec(add)
# print(z())

z=dec(sub)
sub(10,20)'''

# 3. Calculating required time to run the decorator.
import datetime,time
s = time.time()
print("Execution started...")
def dec(x):
    def inner():
        print("Decoration started..")
        x()
        print("Decoration Ended..!!")
    return inner
e = time.time()
diff = e - s 
print("Execution ended ...!!")

def code():
    print("PYTHON")

def cpp():
    print("CPP")

a = dec(code)
a()
print("Timing:- ",diff)