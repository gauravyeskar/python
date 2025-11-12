# Calling the calci module

from Calci import *
print("Enter Choices are:- ")
print("-"*50)
print("for Addition:\t\t\t1")
print("for Substraction:\t\t2")
print("for Multiplition:\t\t3")
print("for Division:\t\t\t4")
print("for Floor Division:\t\t5")
print("for Modulos:\t\t\t6")
print("for Exponent/ Power:\t\t7")
print("-"*50)
ch = int(input(("Enter Your Choice:- ")))
print("-"*50)
match(ch):
    case 1:
        add()
    case 2:
        sub()
    case 3:
        mul()
    case 4:
        div()
    case 5:
        floordiv()
    case 6:
        mod()
    case 7:
        expo()
