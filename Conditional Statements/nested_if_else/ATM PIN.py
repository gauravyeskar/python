pin = int(input("Enter your PIN: "))
ps = 12345
amt = 10000
if(pin == ps):
    print("Correct Pin")
    withdraw =int(input("Enter amount you want to withdrawl: "))
    balance = amt - withdraw
    if(balance > 500):
        print("Payment successfully withdrawl. Your balance amount is: ",balance)
    else:
        print("Insufficient Amount.")
        print("Minimum amout after withdrawl should be minimum 500 Rs.")
        print("Your balance is: ",amt)
else:
    print("Invalid Pin. Please Try again..")