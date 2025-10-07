def gst():
    ta = int(input("Enter the total amount: "))
    gst = int(input("Enter the GST amount: "))
    #gst_per = gst * 100
    aa = ta / (1+(gst/100))
    gst_amt = ta - aa
    cgst = gst_amt // 2
    sgst = cgst 
    print("*"*40)
    print("The total amount is: ",ta)
    print("*"*40)
    print("Discount amount: ",gst_amt)
    print("*"*40)
    print("The CGST amount is: ",cgst)
    print("The sgst amount is: ",sgst)
    print("*"*40)
    print("The actual amount to pay is: ",aa)
    print("*"*40)

gst()