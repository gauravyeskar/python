# Print Hello world program
'''print("Hello World")'''

# Print "Hello world" program using escape sequence
'''print('"Hello World"')'''

# W.a.p.t. perform addition of two no. entered through the keyboard.
'''x = int(input("Enter the Num1:- "))
y = int(input("Enter the Num2:- "))
c = x+y
print("Addition is:- ",c)'''

# W.a.p.t. calculate the simple interest for any principle amount.
'''amount = float(input("Enter the Actual amount:- "))
rate = float(input("Enter the rate of interest:- "))
time = float(input("Enter the time:- "))
si = (amount*rate*time)/100
print("Simple Interest is:- ",si)'''

# W.a.p.t. calculate the average of five subject marks.
'''eng = int(input("Enter the English marks:- "))
math = int(input("Enter the Maths marks:- "))
sci = int(input("Enter the Science marks:- "))
hist = int(input("Enter the History marks:- "))
geo = int(input("Enter the Geography marks:- "))
avg = (eng+math+sci+hist+geo)/5
print("Average of 5 subjects is:- ",avg)  '''

#Ramesh’s basic salary is input through the keyboard. His dearness allowance is 40% of basic 
# salary, and house rent allowance is 20% of basic salary. WAP to calculate his gross salary.  
'''sal = int(input("Enter the Salary:- "))
allowance = sal-((sal*40)/100)
house = sal - (allowance * 20)/100
print("Gross Salary:- ",house)'''

# W.a.p.t. calculate area of circle and rectangle 
'''r = float(input("Enter the Radius:- "))
pi = 3.14
area = pi * r * r
print("Area of Circle: ",area)

l = float(input("Enter the length:- "))
b = float(input("Enter the breadth:- "))
h = float(input("Enter the height:- "))
rect_area = l * b * h
print("Area of rectangle:- ",rect_area)'''

# W.a.p. to swap the two numbers 
'''a = int(input("Enter the num1:- "))
b = int(input("Enter the num2:- "))
b,a=a,b
print("A:- ",a)
print("B:- ",b)'''

# 9. Enter the four Digits no. through the Keyboard? WAP to find the sum of its first and last Digit. 
'''a = 1234
sum = 0
last = a%10
first = a//1000
print(first+last)'''

# 10. Enter the four Digits no. through the Keyboard? WAP to find the sum of its Middle two Digits. 
'''a = 1234
sum = 0
st = str(a)
mid = st[2:4]
for i in mid:
    sum += int(i)
print(sum)'''

# 11. Enter the four Digits no. through the Keyboard? WAP to find the sum of its all digits.
'''a = 1234
sum = 0
st = str(a)
for i in st:
    sum += int(i)
print(sum)'''

# 12. Enter the four Digits no through the Keyboard? Write a program to reverse the No. 
'''a = 1234
st = str(a)
rev = st[::-1]
print(rev)'''

# If a five-digit number is input through the keyboard, write a program to print a new number 
# by adding one to each of its digits. For example if the number that is input is 12391 then the 
# output should be displayed as 23402. 
a = 12345
st = str(a)

    