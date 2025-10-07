h=int(input("Please enter your Hindi marks: "))
e=int(input("Please enter your English marks: "))
m=int(input("Please enter your Maths marks: "))
s=int(input("Please enter your Science marks: "))
so=int(input("Please enter your Social Science marks: "))
countinvalid=0
if(h<0 or h>100 or e<0 or e>100 or m<0 or m>100 or s<0 or s>100 or so<0 or so>100):
    if(h<0 or h>100):
        print("Hindi: Invalid Entry")
        countinvalid+=1
    if(e<0 or e>100):
        print("English: Invalid Entry")
        countinvalid+=1
    if(m<0 or m>100):
        print("Maths: Invalid Entry")
        countinvalid+=1
    if(s<0 or s>100):
        print("Science: Invalid Entry")
        countinvalid+=1
    if(so<0 or so>100):
        print("Social Science: Invalid Entry")
        countinvalid+=1
    print("Invalid input in", countinvalid, "subjects. Please enter valid marks.")
else:
    countfail=0
    countgrace=0
    if(h<36 or e<36 or m<36 or s<36 or so<36):
        if(h<36):
            countfail+=1
            print("Hindi: Fail")
        if(e<36):
            countfail+=1
            print("English: Fail")
        if(m<36):
            countfail+=1
            print("Maths: Fail")
        if(s<36):
            countfail+=1
            print("Science: Fail")
        if(so<36):
            countfail+=1
            print("Social Science: Fail")
        print("Failed in ", countfail,"subjects")
        if(countfail==1):
            if(h>=31 and h<=35):
                countgrace+=1
                if(h==31):
                    print("Grace Marks of 5 awarded")
                    print("Final Hindi Marks: 36")
                elif(h==32):
                    print("Grace Marks of 4 awarded")
                    print("Final Hindi Marks: 36")
                elif(h==33):
                    print("Grace Marks of 3 awarded")
                    print("Final Hindi Marks: 36")
                elif(h==34):
                    print("Grace Marks of 2 awarded")
                    print("Final Hindi Marks: 36")
                else:
                    print("Grace Marks of 1 awarded")
                    print("Final Hindi Marks: 36")
            elif(e>=31 and e<=35):
                countgrace+=1
                if(e==31):
                    print("Grace Marks of 5 awarded")
                    print("Final English Marks: 36")
                elif(e==32):
                    print("Grace Marks of 4 awarded")
                    print("Final English Marks: 36")
                elif(e==33):
                    print("Grace Marks of 3 awarded")
                    print("Final English Marks: 36")
                elif(e==34):
                    print("Grace Marks of 2 awarded")
                    print("Final English Marks: 36")
                else:
                    print("Grace Marks of 1 awarded")
                    print("Final English Marks: 36")
            elif(m>=31 and m<=35):
                countgrace+=1
                if(m==31):
                    print("Grace Marks of 5 awarded")
                    print("Final Maths Marks: 36")
                elif(m==32):
                    print("Grace Marks of 4 awarded")
                    print("Final Maths Marks: 36")
                elif(m==33):
                    print("Grace Marks of 3 awarded")
                    print("Final Maths Marks: 36")
                elif(m==34):
                    print("Grace Marks of 2 awarded")
                    print("Final Maths Marks: 36")
                else:
                    print("Grace Marks of 1 awarded")
                    print("Final Maths Marks: 36")
            elif(s>=31 and s<=35):
                countgrace+=1
                if(s==31):
                    print("Grace Marks of 5 awarded")
                    print("Final Science Marks: 36")
                elif(s==32):
                    print("Grace Marks of 4 awarded")
                    print("Final Science Marks: 36")
                elif(s==33):
                    print("Grace Marks of 3 awarded")
                    print("Final Science Marks: 36")
                elif(s==34):
                    print("Grace Marks of 2 awarded")
                    print("Final Science Marks: 36")
                else:
                    print("Grace Marks of 1 awarded")
                    print("Final Science Marks: 36")
            elif(so>=31 and so<=35):
                countgrace+=1
                if(so==31):
                    print("Grace Marks of 5 awarded")
                    print("Final Social Science Marks: 36")
                elif(so==32):
                    print("Grace Marks of 4 awarded")
                    print("Final Social Science Marks: 36")
                elif(so==33):
                    print("Grace Marks of 3 awarded")
                    print("Final Social Science Marks: 36")
                elif(so==34):
                    print("Grace Marks of 2 awarded")
                    print("Final Social Science Marks: 36")
                else:
                    print("Grace Marks of 1 awarded")
                    print("Final Social Science Marks: 36")
        if(countfail<=3 and countgrace==0):
            print("Candidate is qualified for Ruk Jana Nahi Scheme.")
            print("Re-exam.")
            print("Please enter new marks.")
            h=int(input("Please enter your Hindi marks: "))
            e=int(input("Please enter your English marks: "))
            m=int(input("Please enter your Maths marks: "))
            s=int(input("Please enter your Science marks: "))
            so=int(input("Please enter your Social Science marks: "))
            if(h<0 or h>100 or e<0 or e>100 or m<0 or m>100 or s<0 or s>100 or so<0 or so>100):
                if(h<0 or h>100):
                    print("Hindi: Invalid Entry")
                    countinvalid+=1
                if(e<0 or e>100):
                    print("English: Invalid Entry")
                    countinvalid+=1
                if(m<0 or m>100):
                    print("Maths: Invalid Entry")
                    countinvalid+=1
                if(s<0 or s>100):
                    print("Science: Invalid Entry")
                    countinvalid+=1
                if(so<0 or so>100):
                    print("Social Science: Invalid Entry")
                    countinvalid+=1
                print("Invalid input in", countinvalid, "subjects. Please enter valid marks.")
            else:
                if(h<36 or e<36 or m<36 or s<36 or so<36):
                    print("Grade: Fail even after re-exam")
                else:
                    tot=h+e+m+s+so
                    per=tot/5
                    print("Total Marks: ", tot)
                    print("Percentage: ", per)
                    if(per>=91 and per<=100):
                        print("Grade: A+")
                    elif(per>=81 and per<=90):
                        print("Grade: A")
                    elif(per>=71 and per<=80):
                        print("Grade: B+")
                    elif(per>=61 and per<=70):
                        print("Grade: B")
                    elif(per>=51 and per<=60):
                        print("Grade: C+")  
                    elif(per>=41 and per<=50):
                        print("Grade: C")
                    else:
                        print("Grade: D")
        if(countfail>=4):
            tot=h+e+m+s+so
            per=tot/5
            print("Total Marks: ", tot)
            print("Percentage: ", per)
            print("Grade: Fail")
    else:
        tot=h+e+m+s+so
        per=tot/5
        print("Total Marks: ", tot)
        print("Percentage: ", per)
        if(per>=91 and per<=100):
            print("Grade: A+")
        elif(per>=81 and per<=90):
            print("Grade: A")
        elif(per>=71 and per<=80):
            print("Grade: B+")
        elif(per>=61 and per<=70):
            print("Grade: B")
        elif(per>=51 and per<=60):
            print("Grade: C+")  
        elif(per>=41 and per<=50):
            print("Grade: C")
        else:
            print("Grade: D")