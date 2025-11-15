# .isdigit(): 
'''s = input("Enter the String: ")
digit = False
for i in s:
    if(48 <= ord(i) >= 57):
        digit = True
        break
if digit:
    print("False")
else:
    print("True")'''

# .isdecimal():-
'''s = input("Enter the string: ")
decimal = True
for i in s:
    if not (48<=ord(i)<=57):
        decimal = False
        break
if decimal:
    print("True")
else:
    print("False") '''

# .isalpha():-
''' s=' abc'
space = True
for i in s:
    if not (ord(i)==32):
        space = False
        break
if space:
    print("True")
else:
    print("False") '''

# .isalnum():-
''' s = "a1A"
alnum = True
for i in s:
    if not ((65 <= ord(i) <=90) or (48 <=ord(i)<= 57) or (97 <= ord(i)<= 122)):
        alnum = False
        break
if alnum:
    print("True")
else:
    print("False") '''

# .isupper():
'''s =input("Enter the string: ")
upper = False
for i in s:
    if(65 <= ord(i) >= 97):
        upper = True
        break
if upper:
    print("False")
else:
    print("True") '''

# .islower():- 
''' s = 'abcD'
lower = True
for i in s:
    if not (97<=ord(i)<=122):
        lower = False
        break
if lower:
    print("True")
else:
    print("False") '''

# .isspace():-
''' s = ' '
space = False
for i in s:
    if i == " ":
        space = True
        break
if space:
    print("True")
else:
    print("False") '''

# .isnumeric():-

# .isascii():-
s = '@!#'
asciii = False
for i in s:
    if(0<= ord(i) <= 127):
        asciii = True
        break
if asciii:
    print("True")
else:
    print("false")
print("*"*20)