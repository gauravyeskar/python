n = int(input("Enter the number: "))
a = n%10
b= (n//10)%10
c= n//100

print(a)
print(b)
print(c)
if(a==c and b==b and c == a):
    print("Palindrome")
else:
    print("Not palindrome")
