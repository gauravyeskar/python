username = 'gaurav@121'
ps = 121121
usernam = str(input("Enter the Username: "))
if(username == usernam):
    pss = int(input("Enter Password: "))
    if(ps == pss):
        print("Login Successfully.")
    else:
        print("wrong Password.")
else:
    print("User Not Found.")