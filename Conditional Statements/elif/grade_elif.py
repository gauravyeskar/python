hin = int(input("Enter hindi marks out of 100: "))
eng = int(input("Enter English marks out of 100: "))
mat = int(input("Enter Maths marks out of 100: "))
ss = int(input("Enter social science marks out of 100: "))
sci = int(input("Enter Science marks out of 100: "))
total = hin+ eng+mat+ss+sci
per = (total / 500) * 100
print("Your percentage is: ",per)
if(91 <= per <=100):
    print("Grade A +.")
elif(81 <= per <= 90):
    print("Grade A.")
elif(71 <= per <= 80):
    print("Grade B+.")
elif(61 <= per <= 70):
    print("Grade B.")
elif(51 <= per <= 60):
    print("Grade C+.")
elif(41 <= per <=50):
    print("Grade C.")
elif(36 <= per <= 40):
    print("Grade D.")
else:
    print("...FAIL...")
