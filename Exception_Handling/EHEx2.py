# Multi-Exceptions Handling Block.
try:
    print("Program Execution Started...")
    s1 = input("Enter the first value:- ")
    s2 = input("Enter the second value:- ")
    a = int(s1)
    b = int(s2)
    c = a/b
except(ZeroDivisionError,ValueError,NameError):
    print("Can't Divide by zero. Please Enter a positive number.")
    print("Don't Enter alnums,strs and symbols.")
    print("Variable is not defined.")
else:
    print("-"*50)
    print("Division is:- ",c)
    print("-"*50)
finally:
    print("Program Execution Ended...!!")
    print("*"*50)