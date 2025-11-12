f=open("minor_Project.txt",mode='w')
lst = input("Enter the String: ")
f.write(lst)
f.close()

f=open("minor_project.txt",mode='r')
x=f.read()
alphacount = 0
alphabets = []

digitcount = 0
digits =[]

# 1. Seperate alphabets and digits from the string
for i in lst:
    if i.isalpha():
        alphacount +=1
        alphabets.append(i)
    elif i.isdigit():
        digitcount +=1
        digits.append(i)

# 2. Check Upper Lower
lowercount = 0
loweralphas = []

uppercount = 0
upperalphas =[]

for i in alphabets:
    if i.islower():
        lowercount +=1
        loweralphas.append(i)
    elif i.isupper():
        uppercount +=1
        upperalphas.append(i)

# For Vowels and Consonants
lowervowel = 0
lowervowel_alpha = []
lowerconsonant = 0
lowerconsonants_alpha = []

for i in loweralphas:
    if i in "aeiou":
        lowervowel += 1
        lowervowel_alpha.append(i)
    else:
        lowerconsonant += 1
        lowerconsonants_alpha.append(i)

UPPERvowel = 0
UPPERvowel_alpha = []
UPPERconsonant = 0
UPPERconsonants_alpha = []
for i in upperalphas:
    if i in "AEIOU":
        UPPERvowel += 1
        UPPERvowel_alpha.append(i)
    else:
        UPPERconsonant += 1
        UPPERconsonants_alpha.append(i)


# 3. Seperate even and odd 
evencount = 0
even_nums = []
oddcount = 0
odd_nums = []

for num in digits:
    i = int(num)
    if i%2==0:
        evencount +=1
        even_nums.append(i)
    else:
        oddcount +=1
        odd_nums.append(i)

# 4. For checking prime numbers
primecount = 0
nonprimecount = 0
prime_nums = []
non_prime_nums = []
for d in digits:
    i = int(d)
    if i > 1:
        is_prime = True
        for j in range(2,i):
            if i%j == 0:
                is_prime = False
                break
        
        if is_prime:
            primecount += 1
            prime_nums.append(i)
        else:
            nonprimecount += 1
            non_prime_nums.append(i)
    else:
        nonprimecount += 1
        non_prime_nums.append(i)

# 4. Palindrome Number
palindromecount = 0
palindrome_nums = []
nonpalindromecount = 0
nonpalindrome_nums = []
for i in digits:
        if i == i[::-1]:
            palindromecount += 1
            palindrome_nums.append(int(i))
        else:
            nonpalindromecount +=1
            nonpalindrome_nums.append(int(i))

#####################################################################################
with open('Summary.txt','w') as op:

    op.write("\t*****************************************************************************************\n")
    op.write("\t ALPHABETS ANALYSIS \n")
    op.write("\t*****************************************************************************************\n")
    op.write(f"Total Length of string is:- {len(lst)}\n")
    op.write(f"Total Alphabets are:- {alphacount}\n")
    op.write(f"Alphabets are:- {alphabets}\n")
    op.write("******************************************************************************************\n")

    op.write(f"Total Lower Alphabets are:- {lowercount}\n")
    op.write(f"Lower Alphabets are:- {loweralphas}\n")
    op.write(f"Total Lower Vowels:- {lowervowel}\n")
    op.write(f"Lower Vowels are:- {lowervowel_alpha}\n")
    op.write(f"Total Lower Consonants:- {lowerconsonant}\n")
    op.write(f"Lower Consonants are:- {lowerconsonants_alpha}\n")
    op.write("******************************************************************************************\n")

    op.write(f"Total Upper Alphabets are :- {uppercount}\n")
    op.write(f"Upper Alphabets are:- {upperalphas}\n")
    op.write(f"Total Upper Vowels:- {UPPERvowel}\n")
    op.write(f"Upper Vowels are:- {UPPERvowel_alpha}\n")
    op.write(f"Total Upper Consonants:- {UPPERconsonant}\n")
    op.write(f"Upper Consonants are:- {UPPERconsonants_alpha}\n")

    op.write("\t*****************************************************************************************\n")
    op.write("\t DIGITS ANALYSIS \n")
    op.write("\t*****************************************************************************************\n")
    op.write(f"Total Digits are:- {digitcount}\n")
    op.write(f"Digits are:- {digits}\n")
    op.write("******************************************************************************************\n")
    op.write(f"Total Even Numbers are:- {evencount}\n")
    op.write(f"Even Numbers are:- {even_nums}\n")
    op.write(f"Total Odd Numbers are:- {oddcount}\n")
    op.write(f"Odd Numbers are:- {odd_nums}\n")
    op.write("******************************************************************************************\n")
    op.write(f"Total Prime Numbers:- {primecount}\n")
    op.write(f"Prime Numbers are:- {prime_nums}\n")
    op.write(f"Total Non-Prime Numbers:- {nonprimecount}\n")
    op.write(f"Non-Prime Numbers are:- {non_prime_nums}\n")
    op.write("******************************************************************************************\n")
    op.write(f"Total Palindrome Numbers:- {primecount}\n")
    op.write(f"Palindrome Numbers are:- {palindrome_nums}\n")
    op.write(f"Total Non-Palindrome Numbers:- {nonpalindromecount}\n")
    op.write(f"Non-Palindrome Numbers are:- {nonpalindrome_nums}\n")
    op.write("******************************************************************************************\n")
    op.write(x)
f.close()
print("Data Inserted Successfully...!!")