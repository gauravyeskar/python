a1 = int(input("Enter 1st Angle: "))
a2 = int(input("Enter 2nd Angle: "))
a3 = int(input("Enter 3rd Angle: "))
s1 = a1 + a2
s2 = a1 + a3
s3 = a2 + a3
if(s1 > a3 < s2 > a3 < s3):
    if(a1 == a2 == a3):
        print("Equilateral Triangle.")
    if(a1 == a2 and a1 == a3 or a2 == a1  and a2 == a3 or a3 == a1 and a3 == a2):
        print("Isosceles Triangle.")
    else: 
        print("Scalene Triangle.")
else: 
    print("Invalid ")