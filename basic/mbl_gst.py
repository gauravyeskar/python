ta = int(input("Enter the total amount: "))
gst = 18
gst_per = gst * 100
aa = ta - gst_per
cgst = gst_per // 2
sgst = cgst 
print("The total amount is: ",ta)
print("Discount amount: ",gst_per)
print("The CGST amount is: ",cgst)
print("The sgst amount is: ",sgst)
print("*"*40)
print("The actual amount to pay is: ",aa)
