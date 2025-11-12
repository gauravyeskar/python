# As alias name will caturing the message in the error.
try:
    print("*"*40)
    print("Program Execution Started...")
    s1 = input("Enter the first value:- ")
    s2 = input("Enter the second value:- ")
    a = int(s1)
    b = int(s2)
    c = a/b
except ZeroDivisionError as z:
    print(z)
except ValueError as v:
    print(v)
else:
    print('Division is:- ',c)
finally:
    print("Program Execution Ended..!!")
    print("*"*40)
    print(type(ZeroDivisionError))