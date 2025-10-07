#  input three angles; if sum 180 then classify: right‑angle (one 90), obtuse (one>90), acute (all<90); else “Not triangle”.
a1 = int(input("Enter the 1st angle: "))
a2 = int(input("Enter the 2nd Angle: "))
a3 = int(input("Enter the 3rd Angle: "))
sum = a1+a2+a3
if(sum >= 180):
    print("Your triangle is being classified.")
elif(sum - 90):
    print("one Right angle") 
elif(sum > 90):
    print("One Obtuse angle")
elif(sum < 90):
    print("Acute Angle")
else:
    print("Not Triangle")