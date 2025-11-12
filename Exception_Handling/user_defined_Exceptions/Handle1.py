# Handling the exception by zero is denominator-main program.
from gen1 import divop
from Dev1 import PinError
a = int(input("Enter the first value:- "))
b = int(input("Enter the second value:- "))
try:
    res = divop(a,b)
except PinError:
    print("Can't Divide by Zero.")
else:
    print("Division is:- ",res) # Function call result of exception.
