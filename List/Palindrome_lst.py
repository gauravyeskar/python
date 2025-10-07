# Palindrome
s = int(input("Enter the Size: "))
l = []
rev = []
for i in range(0,s):
    val = int(input("Enter the value: "))
    l.append(val)
print("Straight list: ",l)

for j in range(s-1,-1,-1):
    rev.append(l[j])
print("Reverse list: ",rev)
if(l == rev):
    print("Palindrome.")
else:
    print("Not Palindrome.")