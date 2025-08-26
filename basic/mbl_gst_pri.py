ta = int(input("Enter the total amount: "))
gst = 18
#gst_per = gst * 100
aa = ta / (1+(gst/100))
gst_amt = ta - aa
cgst = gst_amt // 2
sgst = cgst 
print("The total amount is: ",ta)
print("*"*40)
print("Discount amount: ",gst_amt)
print("*"*40)
print("The CGST amount is: ",cgst)
print("The sgst amount is: ",sgst)
print("*"*40)
print("The actual amount to pay is: ",aa)
print("*"*40)



