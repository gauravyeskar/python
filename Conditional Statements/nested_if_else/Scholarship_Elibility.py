gpa = float(input("Enter the gpa: ")) 
if(gpa >= 3.0):
    extra_act = int(input("Enter the extracurricular Activities: "))
    if(extra_act >= 50):
        print("Full Scholarship")
    else:
        print("Partial Scholarship")
else:
    print("Not Eligible")