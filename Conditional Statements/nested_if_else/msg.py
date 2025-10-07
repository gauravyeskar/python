hin = int(input("Enter the Hindi marks: "))
eng = int(input("Enter the English marks: "))
math = int(input("Enter the Maths marks: "))
sos = int(input("Enter the Social social marks: "))
sci = int(input("Enter the Science marks: "))
print("*"*60)
invalid_count  = 0
grace_marks = 0
grace_count = 0 
fail_count = 0

if(100 >= hin >= 36 and 100 >= eng >= 36 and 100 >= math >= 36 and 100 >= sos >= 36 and 100 >= sci >= 36):
    total_marks = hin + eng + math + sos + sci
    per = total_marks / 5
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
    
    print("Total Marks :- ", total_marks)
    print("Percentages:- ",per)
else: 
    # for hindi only for invalid marks and invalid count
    if(hin >= 100 or hin <= 0):
        print("Invalid marks of Hindi. ")
        print("*" * 60)
        invalid_count +=1

    # for English only for invalid marks and invalid count
    if(eng >= 100 or eng <= 0):
        print("Invalid marks of English. ")
        print("*" * 60)
        invalid_count +=1

    # for Maths only for invalid marks and invalid count
    if(math >= 100 or math <= 0):
        print("Invalid marks of Maths. ")
        print("*" * 60)
        invalid_count +=1

    # for Social-Science only for invalid marks and invalid count
    if(sos >= 100 or sos <= 0):
        print("Invalid marks of Social-Science. ")
        print("*" * 60)
        invalid_count +=1 

    # for Science only for invalid marks and invalid count
    if(sci >= 100 or sci <= 0):
        print("Invalid marks of Science. ")
        print("*" * 60)
        invalid_count +=1  
  
    # for English only for invalid marks and invalid count and taking new inputs                                                         
    if(hin<=0 or hin >= 100 ):
        hin= int(input("Enter correct marks for Hindi: "))
        if(hin >=0 and hin <=100):
            #print("Valid marks")
            pass
        else:
            print("Invalid marks for Hindi.")
    
    # for English only for invalid marks and invalid count and taking new inputs
    if(eng >= 100 or eng <= 0 ):
        #print("Invalid marks for English.")
        #invalid_count +=1
        eng= int(input("Enter correct marks for English: "))
        if(eng >= 0 and eng <= 100):
            #print("Valid marks")
            pass
        else:
            print("Invalid marks for English.")

    # for maths only for invalid marks and invalid count and taking new inputs
    if(math >= 100 or math <= 0 ):
        #print("Invalid marks for Maths.")
        #invalid_count +=1
        #print("Invalid count:- ",invalid_count)
        math = int(input("Enter correct marks for Math: "))
        if(math >= 100 and math <= 100):
            #print("Valid marks")
            pass
        else:
            print("Invalid marks for math.")
    
    # for Social-Science only for invalid marks and invalid count and taking new inputs
    if(sos >= 100 or sos <= 0 ):
       #print("Invalid marks for Social-Science.")
        #invalid_count +=1
        #print("Invalid count:- ",invalid_count)
        sos= int(input("Enter correct marks for Social-Science: "))
        if(sos >= 0 and sos <= 100):
            #print("Valid marks")
            pass
        else:
            print("Invalid marks for Social-Science.")
 
    # for Science only for invalid marks and invalid count and taking new inputs
    if(sci >= 100 or sci <= 0 ):
        #print("Invalid marks for Science.")
        #invalid_count +=1
        #print("Invalid count:- ",invalid_count)
        sci = int(input("Enter correct marks for Science: "))
        if(sci >= 0 and sci <= 100):
            #print("Valid marks")
            pass
        else:
            print("Invalid marks for Science.")

    # Just grace_count is counting 
    if(hin > 31 and hin < 36):
        grace_count +=1

    if(eng > 31 and eng < 36):
        grace_count +=1

    if(math > 31 and math < 36):
        grace_count +=1

    if(sos > 31 and sos < 36):
        grace_count +=1

    if(sci > 31 and sci < 36):
        grace_count +=1

    #condition for whether all subject is between the range of 31-35
    if(grace_count <=3):
            if(31 < hin < 36 or 31 < eng < 36 or 31 < math < 36 or 31 < sos < 36 or 31 < sci < 36):
        # For hindi grace_marks.
                if(hin < 36):
                    grace_marks = 36 - hin
                    hin = hin + grace_marks
                    print("Grace of ",grace_marks,"is applied for Hindi.")
                    print("Pass in hindi.")
                    print("Hindi marks: ",hin)
                    print("Grace Count:",grace_count)
                
        # For English grace_marks.
                if(eng < 36):
                    grace_marks = 36 - eng
                    eng = grace_marks + math
                    print("Grace of ",grace_marks,"is applied for English.")
                    print("Pass in English.")
                    print("English marks: ",eng)
                    print("Grace Count:",grace_count)       
    
        # For Maths grace_marks.
                if(math < 36):
                    grace_marks = 36 - math
                    math = grace_marks + math
                    print("Grace of ",grace_marks,"is applied for Maths.")
                    print("Pass in Maths.")
                    print("Maths marks: ",math)
                    print("Grace Count:",grace_count)
                
        # For Social-science grace_marks.
                if(sos < 36):
                    grace_marks = 36 - sos
                    sos = grace_marks + sos
                    print("Grace of ",grace_marks,"is applied for Social-Science.")
                    print("Pass in Social-Science.")
                    print("Social-Science marks: ",sos)
                    print("Grace Count:",grace_count)
            
        # For Science grace_marks.
                if(sci < 36):
                    grace_marks = 36 - sci
                    sci = grace_marks + sos
                    print("Grace of ",grace_marks,"is applied for Social-Science.")
                    print("Pass in Social-science.")
                    print("Social-Science marks: ",sos)
                    print("Grace Count:",grace_count)
                print("*" * 60 )
                if(100 >= hin >= 36 and 100 >= eng >= 36 and 100 >= math >= 36 and 100 >= sos >= 36 and 100 >= sci >= 36):
                    total_marks = hin + eng + math + sos + sci
                    per = total_marks / 5
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
    
                    print("Total Marks :- ", total_marks)
                    print("Percentages:- ",per)
            
            else:
                print("Grade: Fail")
                print("No grace can be given.")
                total_marks = hin + eng + math + sos + sci
                per = total_marks / 5    
                print("Total Marks :- ", total_marks)
                print("Percentages:- ",per)
                if(hin < 31):
                    print("Fail in Hindi.")
                if(eng < 31):
                    print("Fail in English.")
                if(math < 31):
                    print("Fail in Math.")
                if(sos < 31):
                    print("Fail in Social-Science.")
                if(sci < 31):
                    print("Fail in Science.")


        # ******* for RUKH JANA NAHI SCHEME *********
                print("*" * 60)
                print("Your are eligible for *RUKH JANA NAHI SCHEME.* ")
                print("*" * 60)
                if(hin < 31):
                    hin = int(input("Re-enter new marks for hindi: "))
                    if(hin < 31):
                        fail_count+=1
                if(eng < 31):
                    eng = int(input("Re-enter new marks for English: "))
                    if(eng < 31):
                        fail_count+=1
                if(math < 31):
                    math = int(input("Re-enter new marks for Maths: "))
                    if(math < 31):
                        fail_count+=1
                if(sos < 31):
                    sos = int(input("Re-enter new marks for Social-Science: "))
                    if(sos < 31):
                        fail_count+=1
                if(sci < 31):
                    sci = int(input("Re-enter new marks for Science: "))
                    if(sci < 31):
                        fail_count+=1
                
                print("Fail count: ",fail_count)
                print("*" * 60)
                if(fail_count <=3):
                    if(31 < hin < 36 or 31 < eng < 36 or 31 < math < 36 or 31 < sos < 36 or 31 < sci < 36):
                    
        # For hindi grace_marks for RUKH JANA NAHI SCHEME
                        if(hin < 36):
                            grace_marks = 36 - hin
                            hin = hin + grace_marks
                            grace_count+=1
                
        # For English grace_marks for RUKH JANA NAHI SCHEME
                        if(eng < 36):
                            grace_marks = 36 - eng
                            eng = grace_marks + math
                            grace_count+=1     
    
        # For Maths grace_marks for RUKH JANA NAHI SCHEME
                        if(math < 36):
                            grace_marks = 36 - math
                            math = grace_marks + math
                            grace_count+=1
                
        # For Social-science grace_marks for RUKH JANA NAHI SCHEME
                        if(sos < 36):
                            grace_marks = 36 - sos
                            sos = grace_marks + sos
                            grace_count+=1
            
        # For Science grace_marks for RUKH JANA NAHI SCHEME
                        if(sci < 36):
                            grace_marks = 36 - sci
                            sci = grace_marks + sos
                            grace_count+=1

                        if(grace_count <=3):    
                            print("*" * 60 )
                            if(grace_count == 1):
                                print("Grace of ",grace_marks,"is applied for Hindi.")
                                print("Pass in hindi.")
                                print("Hindi marks: ",hin)
                            if(grace_count == 2):
                                print("Grace of ",grace_marks,"is applied for English.")
                                print("Pass in English.")
                                print("English marks: ",eng)  
                            if(grace_count == 3):
                                print("Grace of ",grace_marks,"is applied for Maths.")
                                print("Pass in Maths.")
                                print("Maths marks: ",math)
                            if(grace_count == 4):
                                print("Grace of ",grace_marks,"is applied for Social-Science.")
                                print("Pass in Social-Science.")
                                print("Social-Science marks: ",sos)
                            if(grace_count == 5):
                                print("Grace of ",grace_marks,"is applied for Social-Science.")
                                print("Pass in Social-science.")
                                print("Social-Science marks: ",sos)

                            if(100 >= hin >= 36 and 100 >= eng >= 36 and 100 >= math >= 36 and 100 >= sos >= 36 and 100 >= sci >= 36):
                                total_marks = hin + eng + math + sos + sci
                                per = total_marks / 5
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
                            print("Grade: Fail")
                            print("Fail even after *RUKH JANA NAHI SCHEME* ")
                            print("No grace can be given.")
                            total_marks = hin + eng + math + sos + sci
                            per = total_marks / 5    
                            print("Total Marks :- ", total_marks)
                            print("Percentages:- ",per)
                            print("*" * 60)

                    else:
                        print("*" * 60)
                        print("Fail even after *RUKH JANA NAHI SCHEME*")
                        total_marks = hin + eng + math + sos + sci
                        per = total_marks / 5
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
    
                        print("Total Marks :- ", total_marks)
                        print("Percentages:- ",per)
                        print("*" * 60)
                        print("Please Apply next year.")
                        print("*" * 60)
                else:
                    print("Grade: Fail in *RUKH JANA NAHI SCHEME* ")
                    print("Fail in all subjects...")
                    print("No grace can be given.")
                    total_marks = hin + eng + math + sos + sci
                    per = total_marks / 5    
                    print("Total Marks :- ", total_marks)
                    print("Percentages:- ",per)
                    print("*" * 60)

    total_marks = hin + eng + math + sos + sci
    per = total_marks / 5
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
    print("Total Marks :- ", total_marks)
    print("Percentages:- ",per)
    print("*" * 60)   

elif(grace_count >=3):
    print("Grade: Fail")
    print("Fail in all subjects...")
    print("No grace can be given.")
    total_marks = hin + eng + math + sos + sci
    per = total_marks / 5    
    print("Total Marks :- ", total_marks)
    print("Percentages:- ",per)
    print("*" * 60)