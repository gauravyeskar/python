pin = int(input("Enter Old Pin to update new Pin: "))
old_pin = 12345
if(old_pin == pin):
    print("Correct Pin.")
    new_pin = int(input("Enter new pin: "))
    confirm_pin = int(input("Confirm new pin: "))
    if(new_pin == confirm_pin):
        print("Pin updated")
    else: 
        print("Pin doesn't match.")
        print("Please try again.")
else: 
    print("Invalid Pin.")