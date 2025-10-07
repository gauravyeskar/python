# s = 'nitin'
# rev = ''
# i = len(s)-1
# while(i >= 0):
#     rev = rev+s[i]
#     i-=1
# if(s==rev):
#     print(rev," is a String Palindrome.")
# else:
#     print(rev," is not a string Palindrome.")


s = 'nitin'
rev = ''
l=0
for j in s:
    l+=1
    i=l-1
for i in range(i,-1,-1):
    rev = rev+s[i]
    i-=1
if(s==rev):
    print(rev,"is a string palindrome.")
else:
    print(rev,"is not a string palindrome.")
