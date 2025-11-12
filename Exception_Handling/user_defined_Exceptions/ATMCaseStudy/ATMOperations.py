
from ATMExceptions import DepositError,withDrawError,InsufficientFundError
bal = 500.00
def deposit():
    depoamount = float(input("Enter Your Deposit Amount:- "))
    if depoamount <= 0:
        raise DepositError
    else:
        global bal
        bal += depoamount
        print(f"Your Account XXXXXXX123 Credited with INR: {depoamount}")
        print(f"After Deposit Amount XXXXXXX123 Bal INR: {bal}")

def withdraw():
    global bal
    withdrawamount = float(input("Enter Your Withdraw Amount:- "))
    if withdrawamount <= 0:
        raise withDrawError
    elif withdrawamount+500 > bal:
        raise InsufficientFundError
    else:
        bal -= withdrawamount
        print(f"Your Account XXXXXXX123 Debited with INR: {withdrawamount}")
        print(f"After WithDraw Amount XXXXXXX123 Bal INR: {bal}")

def balEnquiry(): 
    print(f"Your Account XXXXXXX123 Bal INR: {bal}")
