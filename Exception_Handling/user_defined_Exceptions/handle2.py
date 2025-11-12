# W.A.P.Which will generate a multiplication table, where n must be the positive integer value.
# 1. if n == 0: raise zeroerror
# 2. if n < 0: raise NegativeNumberError

from dev2 import ZeroError,NegativeNumberError
from gen2 import table
n = int(input("Enter the Number for generating Table:- "))
try:
    table(n)
except ZeroError:
    print("Can't Divide by zero..")
except NegativeNumberError:
    print("Can't Divide by negative number. Please enter a positive number.")
except ValueError:
    print("Enter a number. No alnums, Symbols and String is allowed.")
