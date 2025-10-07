# Grade Calculator – Marks ke range ke hisaab se grade print karo: A, B, C, D, F.

tm = int(input("Enter the Total marks: "))
match(tm):
    case _ if(91 <= tm <= 100):
        print("Grade A+")
    case _ if(81 <= tm <= 90):
        print("Grade A")
    case _ if(71 <= tm <= 80):
        print("Grade B+")
    case _ if(61 <= tm <= 70):
        print("Grade B")
    case _ if(51 <= tm <= 60):
        print("Grade C+")
    case _ if(36 <= tm <= 50):
        print("Grade D")
    case _ if(36 > tm):
        print("Fail...")
    case __:
        print("Invalid Input.")