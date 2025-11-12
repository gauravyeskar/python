# W.A.P. Which will implement some of the ATM operations and develop, hit and handles the exceptions if required.
from ATMMenu import menu
from ATMOperations import deposit,withdraw,balEnquiry
from ATMExceptions import DepositError,withDrawError,InsufficientFundError
menu()
ch = int(input("Enter Your Choice:- "))
match(ch):
    case 1:
        try:
            deposit()
        except DepositError:
            print("Don't Try to Deposit Zero/Negative Value.")
        except ValueError:
            print("Don't try deposit Alnums, Characters and Symbols.")
        finally:
            print("Thanks For Using My ATM.")
        
    case 2:
        try:
            withdraw()
        except ValueError:
            print("Don't try deposit Alnums, Characters and Symbols.")
        except withDrawError:
            print("Don't try to withdraw zero/ negative value.")
        except InsufficientFundError:
            print("Insufficient Amount..")
        finally:
            print("Thanks For Using My ATM.")
    case 3:
        balEnquiry()
    case 4:
        print("Thanks For Using this.")
    case __ :
        print("Invalid Input.. Try again..!!")