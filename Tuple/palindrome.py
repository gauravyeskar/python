#Palindrome List

s = int(input("Enter the size:- "))
t = ()
pal = 0
no_pal = 0

for i in range(s):
    val = int(input("Enter the values:- "))
    t = list(t)
    t.append(val)
    t = tuple(t)

for j in t:
    temp = j
    rev = 0
    while(j > 0):
        digit = j % 10
        rev = rev * 10 + digit
        j //= 10
    if(temp == rev):
        pal += 1
        print("{} is a palindrome number.".format(temp))
    else:
        no_pal += 1
        print("{} is not a palindrome number.".format(temp))
print("*"*20)
print("Total palindrome count is: ",pal)
print("Total non palindrome count is: ",no_pal)
print("*"*20)