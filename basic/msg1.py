hin = int(input("Enter the Hindi marks: "))
eng = int(input("Enter the English marks: "))
math = int(input("Enter the Maths marks: "))
sos = int(input("Enter the Social social marks: "))
sci = int(input("Enter the Science marks: "))
print('*'*60)
invalid_count = 0 # to count invalid marks
sub_count_nm = ' ' #subject name of invalid count
fail_count = 0 # how many subject are failed
fail_subject = ' ' 
grace_marks = 0 # kitna grace lag raha hai
grace_count = 0
new_total_marks= 0 # marks after rukh jana nai

if(0<= hin <= 100):
    if(31 <= hin <= 36):
        if(grace_count <=3):
            grace_marks = 36 - hin
            grace_count = grace_count + 1
            hin = hin + grace_marks
            print("The grace of:",grace_marks,"is applied in hindi")
        else:
            print("No Grace.")
            fail_count = fail_count+1
    elif(hin <= 31):
        print("Fail in hindi.")
        fail_count = fail_count + 1 # fail subject count
        fail_subject = fail_subject + 'Hindi'
else:
    print("Invalid hindi marks.Please enter correct marks.")
    invalid_count = invalid_count + 1
    sub_count_nm = sub_count_nm + ' hindi '
    print('*'*60)

if(0<= eng <= 100):
    if(31 <= eng <= 36):
        if(grace_count <=3):
            grace_marks = 36 - eng
            grace_count = grace_count + 1
            eng = eng + grace_marks
            print("The grace of:",grace_marks,"is applied in english")
        else:
            print("No Grace.")
            fail_count = fail_count+1
    elif(eng <= 31):
        print("Fail in English.")
        fail_count = fail_count + 1 # fail subject count
        fail_subject = fail_subject + 'English'
else:
    print("Invalid english marks.Please enter correct marks.")
    invalid_count = invalid_count + 1
    sub_count_nm = sub_count_nm + ' english '
    print('*'*60)

if(0<= math <= 100):
    if(31 <= math <= 36):
        if(grace_count <=3):
            grace_marks = 36 - math
            grace_count = grace_count + 1
            math = math + grace_marks
            print("The grace of:",grace_marks,"is applied in math")
        else:
            print("No Grace.")
            fail_count = fail_count+1
    elif(math <= 31):
        print("Fail in Maths.")
        fail_count = fail_count + 1 # fail subject count
        fail_subject = fail_subject + 'Maths'
else:
    print("Invalid maths marks.Please enter correct marks.")
    invalid_count = invalid_count + 1
    sub_count_nm = sub_count_nm + ' math '
    print('*'*60)

if(0<= sos <= 100):
    if(31 <= sos <= 36):
        if(grace_count <=3):
            grace_marks = 36 - sos
            grace_count = grace_count + 1
            sos = sos + grace_marks
            print("The grace of:",grace_marks,"is applied social science")
        else:
            print("No Grace.")
            fail_count = fail_count+1
    elif(sos <= 31):
        print("Fail in sos.")
        fail_count = fail_count + 1 # fail subject count
        fail_subject = fail_subject + 'Social Science'
else:
    print("Invalid sos marks.Please enter correct marks.")
    invalid_count = invalid_count + 1
    sub_count_nm = sub_count_nm + ' sos '
    print('*'*60)

if(0<= sci <= 100):
    if(31 <= sci <= 36):
        if(grace_count <=3):
            grace_marks = 36 - sci
            grace_count = grace_count + 1
            sci = sci + grace_marks
            print("The grace of:",grace_marks,"is applied Science.")
        else:
            print("No Grace.")
            fail_count = fail_count+1
    elif(sci <= 31):
        print("Fail in Science.")
        fail_count = fail_count + 1 # fail subject count
        fail_subject = fail_subject + 'Science'
else:
    print("Invalid science marks.Please enter correct marks.")
    invalid_count = invalid_count + 1
    sub_count_nm = sub_count_nm + ' sci '
    print('*'*60)

if(invalid_count > 0): # dont print if count is 0
    print('The count of invalid subject marks is: ',invalid_count)
    print('The name of invalid subject marks is: ',sub_count_nm)
    print('*'*60)

if(invalid_count == 0): # if inv_cnt == 0 then print only
    total_marks = hin + eng + math + sos + sci
    per = (total_marks / 500) * 100 # percentage calculations
    print("Your total marks is:",total_marks)
    print("Your percentage is:",per)
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
    print("*"*60)
else:
    print("Fail..")
    print("Apply for re-exam.")
    print('*'*60)
    print("--//--//--//--//-//-/-/-///-/-/-/-/-")
    print("You are eligible for RUKH JANA NAHI scheme: ")
    print("Subjects eligible for scheme: ",fail_subject)
    if(hin<=31):
        hin = int(input("Enter new Hindi marks: "))
    if(eng <= 31):
        eng = int(input("Enter new English marks: "))
    if(math <= 31):
        math = int(input("Enter new Maths marks: "))
    if(sos <= 31):
        sos = int(input("Enter new Social Science marks: "))
    if(sci <= 31):
        sci = int(input("Enter new Science marks: "))

# STARTED FOR NEW MARKS.....!!
#if(invalid_count == 0):
        total_marks = hin + eng + math + sos + sci # For new marks input of failed subjects.
        per = (total_marks / 500) * 100 # percentage calculations for new marks.
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
        elif(36 > per):
            print("Fail..")
            print("Apply for re-exam.")
        print('*'*60)

    elif(fail_count > 3):
        print("FAIL...")
        print("You are NOT eligible for RUKH JANA NAHI scheme: ")
        print("Your total marks is: ", total_marks) #if all valid
        print("Your percentage is: ",per) # if all valid
