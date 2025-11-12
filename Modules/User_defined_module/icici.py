bname = "ICICI"
addr = "BULDHANA"
def simple_int():
    p = float(input("Enter the Principle amount: "))
    t = float(input("Enter the Time: "))
    r = float(input("Enter the rate of interest: "))

    si = (p*t*r)/100
    total_amt = p + si
    print("-"*50)
    print("\t Simple Interest Result ")
    print("-"*50)
    print("\t Principal Amount: {}".format(p))
    print("\t Time: {}".format(t))
    print("\t Rate of Interest: {}".format(r))
    print("-"*50)
    print("\t Simple Interest: {}".format(si))
    print("\t Total Amount to pay is {}.".format(total_amt))
    print("-"*50)