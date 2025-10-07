total_amt = 50000
print("Your total amount is: ",total_amt)
amt = int(input("Enter the Amount to Withdrawl: "))
print("Your Balance is: ",total_amt - amt)
if(amt % 100 == 0 or amt % 100 != 0):
    two = amt // 2000
    amt = amt - (two * 2000)
    print("Notes of 2000: ",two)
    
    five = amt // 500
    amt = amt - (five * 500)
    print("Notes of 500: ",five)
    
    one = amt // 100
    amt = amt - (one * 100)
    print("Notes of 100: ",one)

c= two + five + one
print("The total number of notes are: ",c)