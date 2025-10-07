# SET PALINDROME

s = int(input("Enter the size: "))
st = set()
pal_count = 0
no_pal = 0
for i in range(s):
    val = int(input("Enter the value:- "))
    st.add(val)

for j in st:
    temp = j
    rev = 0
    while(j > 0):
        digit = j % 10
        rev = rev * 10 + digit
        j //= 10
    if(temp == rev):
        pal_count +=1
        print("{} is a palindrome number.".format(temp))
    else:
        no_pal += 1
        print("{} is not a palindrome number.".format(temp))
print("*"*30)
print("Total Palindrome count is: ",pal_count )
print("Total not Palindrome count is: ",no_pal)
print("*"*30)