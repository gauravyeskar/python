# Calling and checking and generating the error

from dev2 import ZeroError,NegativeNumberError
def table(n):
    if n== 0:
        raise ZeroError
    
    elif n < 0:
        raise NegativeNumberError
    else:
        print("*"*20)
        print(f"Multiplication Table For {n}")
        for j in range(1,11):
            print(f"{n} X {j} = {n*j}")
        print("*"*20)