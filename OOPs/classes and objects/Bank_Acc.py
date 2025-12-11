# The Bank Account: Create a BankAccount class. The constructor should accept the account_holder_name 
# and an initial balance (default to 0). Add a method deposit(amount) that updates the balance and 
# prints the new balance.
'''import time
class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = 0
        print(f"Account For {self.name} opened with Initial Balance: {self.balance}")
    def deposit(self):
        try:
            depo_bal = int(input("Enter the amount you want to deposit:- "))
            if depo_bal <= 0:
                print("Deposit Failed... Enter positive number.")
            self.balance += depo_bal
            print("Transaction in process...")
            time.sleep(5)
            print(f"Transaction Completed.\nYour Account Balance is: {self.balance}")        
        except:
            print("Error..!! Please contact Your Bank.")

name = input("Enter the Account holder name:- ")
ba1 = BankAccount(name,balance=0)
ba1.deposit()'''

# Static method:- Cannot take self or cls and call be called only with then class name.
class pp:
    @staticmethod
    def students():
        print("Students of Programers Point.")
    def faculty():
        print("PP's Faculty.")
        
pp.students()
pp.faculty()