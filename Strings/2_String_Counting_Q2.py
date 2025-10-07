s = input("Enter the string: ") 
count = 0
for i in s:
    count+=1
l = count
print("The Length of string is {}".format(l))
print("*"*30)

upper_con = 'B','C','D','F','G','H','J','K','L','M','N', 'P','Q','R','S','T','V','W','X','Y','Z'
upper_con_count = 0

lower_con = 'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'
lower_con_count = 0

upper_vow = 'A','E','I','O','U'
upper_vow_count = 0

lower_vow = 'a','e','i','o','u'
lower_vow_count = 0

digit_count = 0
digits = '0','1','2','3','4','5','6','7','8','9'

special_char_count=0
special_characters = '~','!','@','#','$','%','^','&','*','(',')','()'

space= " "
space_count =0


for i in range(0,l,1):
    if s[i] in upper_con:
        upper_con_count += 1
        print(s[i], "is a UPPER and CONSONANT.") 
        print("*"*30)
    
    elif(s[i] in space):
        space_count +=1
        print(s[i],"is a space.")
        print("*"*30)

    elif(s[i] in lower_con):
        lower_con_count +=1
        print(s[i],"is a LOWER and CONSONANT.")
        print("*"*30)

    elif(s[i] in upper_vow):
        upper_vow_count +=1
        print(s[i],"is an UPPER and VOWEL.")
        print("*"*30)

    elif(s[i] in lower_vow):
        lower_vow_count +=1
        print(s[i],"is an LOWER and VOWEL.")
        print("*"*30)

    elif(s[i] in digits):
        digit_count += 1
        print(s[i],"is a DIGIT.")
        print("*"*30)
    
    else:
        special_char_count += 1
        print(s[i],'is a SPECIAL CHARACTER.')
        print("*"*30)

alphabet_count = 0
alphabet_count = upper_con_count + lower_con_count + upper_vow_count + lower_vow_count

print("The total Alphabets are {}".format(alphabet_count))
print("The total UPPER consonants are {}".format(upper_con_count+upper_vow_count))
print("The total LOWER consonants are {}".format(lower_con_count+lower_vow_count))
print("The total DIGITS are {}".format(digit_count))
print("The total SPECIAL CHARACTERS are {}".format(special_char_count))
print("The total Vowels are {}".format(lower_vow_count+upper_vow_count))
print("The total Upper Vowels are {}".format(upper_con_count+lower_con_count))
print("The total SPACES are {}".format(space_count))
print("*"*50)

