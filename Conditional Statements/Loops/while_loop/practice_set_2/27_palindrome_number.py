# Check number is palindrome or not
num = int(input("Enter the number for palindrome: "))
number = num
rev = 0 
while(num > 0):
    ld= num % 10
    rev = rev*10 + ld
    num = num // 10
print(rev)
if(number == rev):
    print("Palindrome number")
else: 
    print("Not Palindrome number")