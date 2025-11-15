# Program for accepting two numbers for user and find 
try:
    print("*"*30)
    print("Program Execution Started...")
    s1 = input("Enter the first value:- ")
    s2 = input("Enter the second value:- ")
    a = int(s1)
    b = int(s2)
    c = a/b
except ZeroDivisionError:
    print("Cannot divide by zero. Give a positive number.")
except ValueError:
    print("Dont enter alnums, strs or symbols.")
else:
    print('Division is:- ',c)
finally:
    print("Program Execution Ended..!!")
    print("*"*40)