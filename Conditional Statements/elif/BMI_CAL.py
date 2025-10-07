#BMI calculator
a = int(input("Enter Your Weight: "))
if(a < 18.5):
    print("Under Weight..")
elif(18.5 < a < 24.9):
    print("Normal..")
elif(25 < a < 29.9):
    print("Over Weight..") 
elif(30 <= a):
    print("Obese..")
else: 
    print("Invalid Input")
    