# Finding sum of the input number.
''' n = int(input("Enter the number: "))
if n<=0:
    print("Invalid number.")
else:
    s = 0
    for i in str(n):
        v = int(i)
        s = s+v
    else:
        print("Digits sum is {} = {}".format(n,s)) '''

# Factorial of a program
''' n = int(input("Enter the number: "))
if n <= 0:
    print("Invalid Number.")
else:
    f = 1
    for i in range(2,n+1):
        f = f * i
    else:
        print("Factorial is {}".format(f)) '''

# reverse Factorial
''' n = int(input("Enter the number: "))
if n <= 0:
    print("Invalid number.")
else:
    f = 1
    for i in range(n,1,-1):
        f = f * i 
    else:
        print("Reverse factorial is {}".format(f)) '''

# Factors of a number
''' n = int(input("Enter the number: "))
if n <= 0:
    print("Invalid Number.")
else:
    for i in range(1,n+1):
        if n%i == 0:
            print("{}".format(i),end=" , ")  '''

# LIST Excessing loop
''' lt = [100,200,300,400,500,600]
print("By using while loop --> forward direction.")
i= 0 
while(i<len(lt)):
    print(lt[i])
    i = i+1
print("By using while loop --> backward direction.")
i = len(lt) -1
while(i>=0):
    print(lt[i])
    i = i-1
print("By using for loop --> forward direction.")
for i in lt:
    print(i)
print("By using for loop --> backward direction.")
for i in lt[::-1]:
    print(i)
print("By using for loop --> backward direction.")
for i in range(-1,-7,-1):
    print(lt[i]) '''

# Table printing
''' n = int(input("Enter the number: "))
if n <= 0:
    print("Invalid Number.")
else:
    print("*"*20)
    print("Multiplication Table for {}".format(n))
    print("*"*20)
    for i in range(1,11):
        print("{} * {} = {}".format(n,i,n*i))
    else:
        print("*"*20) '''

# Program for accepting a line of text and print and count no of vowels.
''' t = input("Enter the Text: ")
count = 0
for i in t:
    if i in ['a','e','i','o','u','A','E','I','O','U']:
        print("{} ".format(i))
        count+=1
else:
    print("Number of vowels are: ",count) '''

# Accessing string by loop
''' s= 'Python'
print("By Using While Loop")
i = 0
while(i<len(s)):
    print(s[i])
    i += 1
print("*"*20)
print("By using For loop")
for i in s:
    print(i)
print("*"*20) '''
