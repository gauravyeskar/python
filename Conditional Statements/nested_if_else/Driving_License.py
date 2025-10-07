age = int(input("Enter age: "))
if(age >= 18):
    L_L = str(input("Have u applied for Learning License: "))
    if (L_L.lower() == 'no'):
        print("Please Apply for Learning License.")
        pan_card = str(input("Do you have pan Card: "))
        if pan_card.lower() == 'yes':
            adrs = str(input("Do you have Adhar Proof: "))
            if adrs.lower() == 'yes':
                print("Immediately apply for learning License.")
            else:
                print("Address ID is compulsory.")
        else:
            print("Pan card is compulsory.")
    else: 
        print("Please Apply for Permanent License.")
        pan_card = str(input("Do you have pan Card: "))
        if pan_card.lower() == 'yes':
            adrs = str(input("Do you have Adhar Proof: "))
            if adrs.lower() == 'yes':
                print("You can apply for Permanent License.")
            else:
                print("Address ID is compulsory.")
        else:
            print("Pan card is compulsory.")
else: 
    print("Not Eligible to drive.")