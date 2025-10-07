num = eval(input("Enter the number:- "))
rev=0
print("Before reverse value: ",num)
while(num>0):
    last_digit = num%10
    rev = rev*10 + last_digit
    num //=10
print("After reverse value:- ",rev)