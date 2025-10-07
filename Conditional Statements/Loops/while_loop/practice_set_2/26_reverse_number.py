# 1234 --> 4321
num = eval(input("Enter the number:- "))
four = num % 10
three = (num // 10) % 10
two = (num//100)%10
one = (num//1000)%10
print(four,three,two,one)

print("*"*20)

rev=0
print("Before reverse value: ",num)
while(num>0):
    last_digit = num%10
    rev = rev*10 + last_digit
    num //=10
print("After reverse value:- ",rev)