pin = 12345
pss = int(input("Enter Password: "))
if(pin == pss):
    print("Login Successfully")
    total_amt = 10000
    print("Your total amount is: ",total_amt)
    amt = int(input("Enter the Amount to Withdrawl: "))
    amount = amt
    if(amt % 100 == 0):
        if(amt < total_amt):
            pss = int(input("Enter the Pin: "))
            if(pin == pss):
                print("Processing...")
    
            
                two_thou = amt // 2000  # 2 = 5000 // 2000
                amt = amt - (two_thou * 2000)  # 1000 = 5000 - 4000
            
                five = amt // 500  
                amt = amt - (five * 500)
        
                two = amt // 200
                amt = amt - (two * 200)
               
                one = amt // 100
                amt = amt - (one * 100)

                print("Notes of 2000  * ",two_thou,": ",two_thou*2000)  
                print("Notes of 500  * ",five,":",five*500) 
                print("Notes of 200 * ",two,":",two*200) 
                print("Notes of 100 * ",one,":",one*100) 
                print("*"*60)
                c= two_thou + five + two + one
                print("Your amount: ",amount)
                print("Your Balance is: ",total_amt - amount)
                print("The total number of notes are: ",c)
                print("*"*60)   
            else:
                print("Wrong Pin. Please Try Again.")
        else:
            print("Insufficient Balance.")
    else:
        print("No 50,20,10 Notes are available.")
else:
    print("Wrong Pin. Please Try Again.")