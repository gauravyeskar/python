# Q-1)Write a program to find the euclidean distance between two coordinates. Take both the coordinates from the user as input.
'''
from math import sqrt
x1 = eval(input("Enter first coordinates (x1) value:- "))
x2 = eval(input("Enter first coordinates (x2) value:- "))

y1 = eval(input("Enter second coordinates (y1) value:- "))
y2 = eval(input("Enter second coordinates (y2) value:- "))

euc_dis = sqrt(((x2-x1)**2)+((y2-y1)**2))

print(f"The Euclidean Distance for 1D is:- {(euc_dis)}")
print("*"*30)   '''

# Q-2)Write a program to find the sum of squares of first n natural numbers where n will be provided by the user.
'''
n = int(input("Enter the natural number to find sum of squares:- "))
sum = 0
if n > 0:
    for i in range(1,n+1):
        sum += i*i

print("The sum of square all the nautral numbers are:- ",(sum))  '''

# Q-3)Given the first 2 terms of an Arithmetic Series. Find the Nth term of the series. Assume all inputs are provided by the user.
'''
a1 = int(input("Enter the first highest value:- "))
a2 = int(input("Enter the second lowest value:- "))
distance = a1 - a2
n = int(input("Enter the nth value:- "))
an = a1 + ((n-1) * distance)
print(f"The {n}th Term of the series is:- {an}") '''

# Q-4)Given 2 fractions, find the sum of those 2 fractions.Take the numerator and denominator values of the fractions from the user.
'''
num1 = int(input("Enter first numerator:- "))
den1 = int(input("Enter first denominator:- "))
num2 = int(input("Enter second numerator:- "))
den2 = int(input("Enter second denominator:- "))
fract_sum = ((num1*den2) + (num2*den1))
densum = (den1 * den2)
print("The sum of both the fractions is:- ",fract_sum , "/",densum) '''

# Q-5)Write a program that will give you in hand monthly salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction as below:
'''
salary = eval(input("Enter Your Anual Salary CTC in rupees:- "))
hra = salary * 0.10
da = salary *0.05
pf = salary * 0.03
total_taxes = hra + da + pf 
anual_sal = (salary - total_taxes)
monthly_sal = (anual_sal / 12)
print("*"*40)
print(f"Your current Anual salary CTC is {salary}")
print(f"your taxes deduction is \n\thra(10%): {hra}\n\tDA(5%) : {da}\n\tPf(3%): {pf}.\nYour Anual in Hand salary will be: {anual_sal}.\nYour Per Month Salary will be: {monthly_sal}") '''

# Q-6)Write a program that take a user input of three angles and will find out whether it can form a triangle or not sum1=0
''' 
sum = 0
for i in range(3):
    n = eval(input("Enter the angles:- "))
    sum +=n
if sum == 180:
    print("It can form triangle.")
else:
    print("It can't form triangle.") '''

# Q-7)Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit.	
'''
cost = eval(input("Enter the cost price:- "))
sale = eval(input("Enter the selling price:- "))
if cost > sale:
    print(f"The loss of {cost - sale} is there." )
else:
    print(f"The profit of {sale - cost} is there.") '''
 

# Q-8)Write a menu-driven program -
''' 
1.cm to ft
2.km to miles
3.USD to INR
4.exit  '''
'''
ch = eval(input("Enter Your choice:- 1. cm to ft. 2. Km to miles. 3. USD to INR. 4. Exit :- "))
match(ch):
    case 1:
        print("Your Choice is Cm to Feet.")
        cm = eval(input("Please Enter the Centimeter:- "))
        feet = cm * 0.032
        print(f"{cm} to feet is {feet}")
    case 2:
        print("Your Choice is Km to Miles.")
        km = eval(input("Please Enter the Kilometer:- "))
        miles = km / 1.609
        print(f"{km} to feet is {miles}")
    case 3:
        print("Your Choice is USD to INR.")
        USD = eval(input("Please Enter the USD:- "))
        INR = USD * 88.63
        print(f"{USD} to feet is {INR}")
    case 4:
        print("You have chosen 4 EXIT.")
        breakpoint
print("Thanks for using.")  '''

# Q-9)Take a user input as integer N. Find out the sum from 1 to N. If any number if divisible by 5,  
# then skip that number. And if tht use for loop to solve te sum is greater than 300, don't need to calculate the sum further 
# more. Print the final result. And don'his problem.
''' 
n = eval(input("Enter the number:- "))
sum = 0 
for i in range(1,n+1):
    if i % 5 == 0:
        continue
    sum = sum + i
    if sum > 300:
        break
print("Sum is:- ",sum) '''

# Q-10)Write a program that keeps on accepting a number from the user until the user enters Zero. Display the sum and average of all the number.
'''
sum = 0
count = 0
avg = 0
while True:
    n = eval(input("Enter the number:- "))
    if n==0:
        break
    else:
        sum +=n
        count +=1
        avg = sum / count
print(f"The sum of {count} numbers are: {sum}.\nAverage of {count} numbers are: {avg}") '''

# Q-11)Write a program which will find all such numbers which are divisible by 7 but are not a 
#      multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a 
#      comma-separated sequence on a single line.
'''
for i in range(2000,3201):
    if(i % 7 == 0 and i * 5 != 0):
        print(i,end=",") '''

# Q-12)Write a program, which will find all such numbers between 1000 and 3000 (both included)
#      such that each digit of the number is an even number. 
#      The numbers obtained should be printed in a space-separated sequence on a single line.
''' 
res = []
for i in range(1000,3001):
    s = str(i)
    if all(int(j)%2==0 for j in s):
    
        res.append(s)
print(" ".join(res)) '''

# 13)Write a program to print the following pattern
'''     1
        2 1
        3 2 1
        4 3 2 1
        5 4 3 2 1   '''
''' 
for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end =" ")
    print('') '''

# 14)Write a Python Program to Find the Sum of the Series till the nth term:
#    1 + x^2/2 + x^3/3 + … x^n/n, n will be provided by the userx = int(input("Enter x: "))
'''
x = eval(input("Enter the constant value:- "))
n = eval(input("Enter the Nth Number:- "))
sum = 0
for i in range(1,n+1):
    sum = (x**i) / i
print("The sum is:- ",sum) '''

# Q-15)Find the sum of the series upto n terms. Write a program to calculate the sum of series up to n term. For example, 
#      if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690. Take the user input and then calculate.
#      And the output style should match which is given in the example.
'''
n = eval(input("Enter the number:- "))
num = ''
sum = 0
for i in range(n):
    num += '2'
    print(num,end=" ")
    sum += int(num)
    if i < n-1:
        print("+",end=" ")
print("= ",sum)  '''


# Q-16)Write a program to print all the unique combinations of 1,2,3 and 4
''' Output:
        1 2 3 4
        1 2 4 3
        1 3 2 4
        1 3 4 2
        1 4 2 3
        1 4 3 2
        2 1 3 4
        2 1 4 3
        2 3 1 4
        2 3 4 1  
        2 4 1 3   '''
''' 
n = [1,2,3,4]
for i in n:
    for j in n:
        if i == j:
            continue
        for k in n:
            if k == i or k == j:
                continue
            for l in n:
                if l == i or l == j or l == k:
                    continue
                print(i,j,k,l) '''

# Q-17)Write a program that will take a decimal number as input and prints out the binary equivalent of the number
'''
n = int(input("Enter the value:- "))
binary = bin(n)
res = str(binary)
res1 = binary[2:]
print(res1) '''

# Q-18)Write a program that will take 2 numbers as input and prints the LCM and HCF of those 2 numbers
'''
from math import lcm,gcd
n1 = int(input("Enter the first value:- "))
n2 = int(input("Enter the second value:- "))
print(gcd(n1,n2))
print(lcm(n1,n2)) '''

# Q-19)Create Short Form from initial character
#   Input:Data science program
#   Output: DSP	 
'''
txt = input("Enter the text:- ")
words = txt.split()
short_form = "".join(word[0].upper() for word in words)
print(short_form) '''

# Q-20)Append second string in the middle of first string
#    Input: paython data
#    Output:Paydatathon
'''
s1 = input("Enter the first string:- ")
s2 = input("Enter the second string:- ")
mid = len(s1)//2
result = s1[:mid] + s2 + s1[mid:] 
print(result) '''

# Q-21)Given string contains a combination of the lower and upper case letters. 
# Write a program to arrange the characters of a string so that all lowercase letters should come first.
#       Given: str1 = PyNaTive
#       Expected Output: yaivePNT
'''
txt = input("Enter the string:- ")
loer=''
uper=''
for i in txt:
    if i.isupper():
        loer += i
    else:
        uper += i
print("Output is: ",uper+loer) '''

# Q-22)Take a alphanumeric string input and print the sum and average of the digits that appear in the string, ignoring all other characters.
#       Input:-hel123O4every093
#       Output: Sum: 22
#       Avg: 2.75
'''
sum = 0
count = 0
avg = 0
s = 'hel123O4every093'
for i in s:
    if i.isdigit():
        sum += int(i)
        count +=1
print("sum:- ",sum)
print("Count:- ",count)   
print("Avg:-",sum/count)   '''

# Q-23)Removal of all characters from a string except integers
# Given: str1 = 'I am 25 years and 10 months old'
# Expected Output: 2510
'''
res = ''
s = input("Enter Alphanumeric values: ")
for i in s:
    if i.isdigit():
        res +=i
print(res)  '''

# Q-24)Reverse words in a given String
#   Input: my name is laxmi
#   Output: laxmi is name my
'''
res =''
s = 'my name is laxmi'
words = s.split()
res = words[::-1]
print(" ".join(res))  '''

# Q-25)Find uncommon words from two Strings.
''' 
Input:
A = "apple banana mango" 
B = "banana fruits mango"
Output:
['apple', 'fruits']  '''
'''
l =[]
a = "apple banana mango" 
b = "banana fruits mango"
a_words = set(a.split())
b_words = set(b.split())

res = a_words.symmetric_difference(b_words)
print(res) '''

# Q-26)Write a program that can remove all the duplicate characters from a string. User will provide the input.
'''
res = ''
txt = input("Enter the string:- ")
for i in txt:
    if i not in res:
        res +=i
print(res)  '''

# Q-27)Combine two lists index-wise(columns wise)
#Given List: list1 = ["M", "na", "i", "Kh"]
#            list2 = ["y", "me", "s", "an"]
#            Output: [['M','y'], ['na', me'], ['i', 's'], ['Kh', 'an']]
'''
list1 = ["M", "na", "i", "Kh"]
list2 = ["y", "me", "s", "an"]
res = [[list1[i],list2[i]]for i in range(len(list1))]
print("Output: ",res)   '''

# Q-28)Add new item to list after a specified item
#   Write a program to add item 7000 after 6000 in the following Python List
#   list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
#   Output: [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
'''
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)  '''

# Q-29)Update no of items available
#   Input:- candy_list = ['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']
#   no_of_items = [10,20,34,74,32]
#   Output: Jelly Belly-10
#   Kit Kat-20
#   Double Bubble-34
'''
candy_list = ['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']
no_of_items = [10,20,34,74,32]
for i in range(3):
    print(candy_list[i] ,'-',no_of_items[i]) '''

# Q-30)Running Sum on list
#   Input: list1 = [1,2,3,4,5,6]
#   Output: [1,3,6,10,15,21]
'''
list1 = [1,2,3,4,5,6]
op = []
sum = 0
for i in list1:
    sum+=i
    op.append(sum)
print(op)  '''

# Q-31)Find list of common unique items from two list. and show in increasing order
#   Input:- num1 = [23,45,67,78,89,34]
#   num2 = [34,89,55,56,39,67]
#   Output:[34, 67, 89]
'''
num1 = [23,45,67,78,89,34]
num2 = [34,89,55,56,39,67]
s_n1 = set(num1)
s_n2 = set(num2)
op = s_n1.intersection(s_n2)
print(list(sorted(op))) '''

# Q-32)Convert Character Matrix to single String using string comprehension.
# Input: [['c', 'h', 'e', 't', 'a', 'n'],['s','i','r'], ['i', 's'], ['b', 'e', 's', 't'],['a'],['t', 'e', 'a', 'c', 'h', 'e', 'r']]
# Output: chetan sir is a best teacher
ip = [['c', 'h', 'e', 't', 'a', 'n'],['s','i','r'], ['i', 's'], ['b', 'e', 's', 't'],['a'],['t', 'e', 'a', 'c', 'h', 'e', 'r']]








# Q-33)Add Space between Potential Words.
#   Example:Input: ['chetanSirIs', 'bestFor', 'dataScientist']
#   Output: ['chetan Sir Is', 'best For', 'data Scientist']
'''
data =  ['chetanSirIs', 'bestFor', 'dataScientist']
op =[]
for d in data:
    wrd = ''
    for i in d:
        if i.isupper():
            wrd += " " + i
        else:
            wrd +=i
    op.append(wrd.strip())    
print("Output:- ",op)   '''

# Q-34)Write a program that can find the max number of each row of a matrix
#   Input:  [[1,2,3],[4,5,6],[7,8,9]]
#   Output:  [3,6,9]
'''
lst = [[10,2,3],[40,5,6],[70,8,9]]
op = [max(rows) for rows in lst]
print(op)   '''

# Q-35)Write a list comprehension that can transpose a given matrix 
''' 
matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]
[1, 4, 7]
[2, 5, 8]
[3, 6, 9]   '''











# Q-38)Check is tuples are same or not?
'''
t1 = (1,2,3,0)
t2 = (1,2,3)
if t1 == t2:
    print("Same")
else:
    print("Differs")   '''

# Q-40)Write a program to find set of common elements in three lists using sets.
'''
Input : ar1 = [1, 5, 10, 20, 40, 80]
        ar2 = [6, 7, 20, 80, 100]
        ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
Output : [80, 20]   '''
'''
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
sar1 = set(ar1)
sar2 = set(ar2)
sar3 = set(ar3)
lst = [sar1.intersection(sar2) and sar2.intersection(sar3) and sar3.intersection(sar1)]
op = str(lst)
print("Output:- ",op)   '''

# Q-41)Sort Python Dictionary by Key or Value.
d = {'c': [3], 'b': [12, 10], 'a': [19, 4]}
print(dict(sorted(d.items())))
