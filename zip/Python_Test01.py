# Q-1)Write a program to find the euclidean distance between two coordinates. Take both the coordinates from the user as input.
'''from math import sqrt
x1= int(input("Enter the value of x1:- "))
y1 = int(input("Enter the value of y1:- "))

x2 = int(input("Enter the value of x2:- "))
y2 = int(input("Enter the value of y2:- "))

Euc_dis = sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"The Euclidean Distance is:- {Euc_dis}")'''

# Q-2)Write a program to find the sum of squares of first n natural numbers where n will be provided by the user.
''' n = int(input("Enter the Nth value for finding natural number:- "))
sum = 0
square = 0
if n > 0:
    for i in range(1,n):
        square = i ** 2
        sum += square
print(f"The sum of squares of {n} natural numbers are:- {sum}") '''

# Q-3)Given the first 2 terms of an Arithmetic Series.Find the Nth term of the series. Assume all inputs are provided by the user.
''' x1 = int(input("Enter the first highest term of Arithmetic Series:- "))
x2 = int(input("Enter the second lowest term of arithmetic series:- "))
diff = x1 - x2
n = int(input("Enter the nth value:- "))
Nth = (x1 + (n-1)* diff)
print(f"The nth value is:- {Nth}")  '''

# Q-4)Given 2 fractions, find the sum of those 2 fractions. Take the numerator and denominator values of the fractions from the user.
'''n1 =  int(input("Enter the 1st Numerator:- "))
d1 = int(input("Enter the 1st Denominator:- "))

n2 = int(input("Enter the 2nd Numerator:- "))
d2 = int(input("Enter the 2nd Denominator:- "))

num_sum = (((n1*d2) + (n2 * d1)))
den_sum = (d1 * d2)

print(f"The sum of the fractions is:- {num_sum} / {den_sum}") '''

# Q-5)Write a program that will give you in hand monthly salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction as below:
''' Anual_sal = float(input("Enter the Anual Salary CTC in Rupees:- "))
hra = Anual_sal * 0.10
DA = Anual_sal * 0.05
PF = Anual_sal * 0.03
total_deduct = hra + DA + PF
inhand_sal_Anual = Anual_sal - total_deduct
monthly_sal = inhand_sal_Anual / 12
print("*"*20)
print("Salary Deduction Below:- ")
print(f"HRA:-  {hra}")
print(f"HRA:-  {DA}")
print(f"HRA:-  {PF}")
print("*"*20)
print(f"Total InHand Anual Salary :- {inhand_sal_Anual}")
print(f"Monthly Salary:- {monthly_sal}") '''

# Q-6)Write a program that take a user input of three angles and will find out whether it can form a triangle or not.
''' a1 = int(input("Enter the first Angle:- "))
a2 = int(input("Enter the Second Angle:- "))
a3 = int(input("Enter the Third angle:- "))

if (a1+a2+a3 == 180):
    print("It Can form a Triangle.")
else:
    print("It Can't Form a Triangle.") '''

# Q-7)Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit.
''' cp = float(input("Enter the cost Price:- "))
sp = float(input("Enter the Selling Price:- "))

if cp > sp:
    loss = cp - sp
    print(f"Loss of {loss} RS. has happened.")

if cp < sp:
    Profit = sp - cp
    print(f"Profit of {Profit} Rs. has happened.") '''

# Q-8)Write a menu-driven program -
'''     1.cm to ft
        2.km to miles
        3.USD to INR
        4.exit '''
''' print("Choices are:\n\t1.cm to ft.\n\t2.km to miles.\n\t3.USD to INR.\n\t4.exit")
ip = int(input("Enter you choice:- "))
print("-"*30)
match(ip):
    case 1:
        print("You have choosen Centimeter to Feet Conversion.")
        cm = float(input("Enter Centimeters:- "))
        feets = cm * 0.032
        print(f"{cm} is {feets}")
    case 2:
        print("You have choosen Kilometer to Miles Conversion.")
        km = float(input("Enter Kilometers:- "))
        miles = km /1.609
        print(f"{km} is {miles}")
    case 3:
        print("You have choosen USD to INR Conversion.")
        usd = float(input("Enter USD:- "))
        inr = usd * 88.63
        print(f"{usd} is {inr}")
    case 4:
        print("You have choosen EXIT.")
        breakpoint
print("Thanks For Using..!!")  '''

#Q-9)Take a user input as integer N. Find out the sum from 1 to N. If any number if divisible by 5, then skip that number. And if the sum is greater than 300, don't need to calculate the sum further more. Print the final result. And don't use for loop to solve this problem.
'''n = int(input("Enter the Nth value:- "))
sum = 0
i = 1
while i <= n:
    if i%5!=0:
        sum += i
    if  sum > 300:
        break
    i+=1
print(f"The sum of {n} number is: {sum}")'''

# Q-10)Write a program that keeps on accepting a number from the user until the user enters Zero. Display the sum and average of all the numbers
''' sum = 0
avg = 0
count = 0
while True:
    n = float(input("Enter the number:- "))
    if n == 0:
        break
    else:
        sum += n
        count +=1
avg = sum / count
print(f"The sum of {count} number is {sum}.")
print(f"the average of {count} numbers is {avg}")   '''

# Q-11)Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.
''' lst = ''
for i in range(2000,3201):
    if i % 7 and i%5 != 0:
        print(i,end=",")  '''

# Q-12)Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number. The numbers obtained should be printed in a space-separated sequence on a single line.
''' lst = []
for i in range(1000,3001):
    s = str(i)
    if all(int(j)%2 == 0 for j in s):
        lst.append(s)
print(" ".join(lst))  '''

# Q-13)Write a program to print the following pattern
''' 1
    2 1
    3 2 1
    4 3 2 1
    5 4 3 2 1 '''
''' for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end=" ")
    print("") '''

# Q-14)Write a Python Program to Find the Sum of the Series till the nth term: 1 + x^2/2 + x^3/3 + … x^n/n. n will be provided by the user
'''n = int(input("Enter the Nth value:- "))
sum= 0
for i in range(1,n):
    sum += (i**n)/n
print(f"The sum is: {sum}")'''
  
#Q-15)Find the sum of the series upto n terms.Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690. Take the user input and then calculate.And the output style should match which is given in the example.
''' n = eval(input("Enter the number:- "))
num = ''
sum = 0
for i in range(n):
    num += '2'
    print(num,end=" ")
    sum += int(num)
    if i < n-1:
        print("+",end=" ")
print("= ",sum)   '''

# Q-16)Write a program to print all the unique combinations of 1,2,3 and 4
# Output:
'''     1 2 3 4
        1 2 4 3
        1 3 2 4 
        1 3 4 2
        1 4 2 3
        1 4 3 2
        2 1 3 4
        2 1 4 3
        2 3 1 4
        2 3 4 1
        2 4 1 3 '''
''' lst = [1,2,3,4]
for i in (lst):
    for j in (lst):
        if i == j:
            continue
        for k in (lst):
                if k == i and k == j:
                    continue
                for l in (lst):
                        if k == i and k == j and k == l:
                            continue
                print(i,j,k,l)   '''

# Q-17)Write a program that will take a decimal number as input and prints out the binary equivalent of the number.
''' n = int(input("Enter the Decimal number:- "))
res = bin(n)
op = res[2:]
print(op)  '''

# Q-18)Write a program that will take 2 numbers as input and prints the LCM and HCF of those 2 numbers
''' from math import lcm,gcd
n1 = int(input("Enter the first value:- "))
n2 = int(input("Enter the second value:- "))
print(gcd(n1,n2))
print(lcm(n1,n2)) '''

# Q-19)Create Short Form from initial character
# Input: Data science program
# Output: DSP 
''' ip='Data science program'
words = ip.split()
res = "".join(word[0].upper() for word in words)
print(res) '''

# Q-20)Append second string in the middle of first string
# Input: paython  data
# Output: paydatathon
''' s1 = 'paython'
s2 = 'data'
mid = len(s1)//2
op = s1[:mid] + s2 + s1 [mid:]
print(op) '''

# Q-21)Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.
#Given: str1 = PyNaTive
#Expected Output: yaivePNT
''' str1 = 'PyNaTive'
upr = '' 
loer = ''
for i in str1:
    if i.isupper():
        upr +=i
    else:
        loer +=i
op = loer + upr
print(op) '''

# Q-22)Take a alphanumeric string input and print the sum and average of the digits that appear in the string, ignoring all other characters.
''' Input:-hel123O4every093
Output: 
Sum: 22
Avg: 2.75  '''

''' txt = 'hel123O4every093'
sum = 0
count = 0
avg = 0
for i in txt:
    if i.isdigit():
        sum += int(i)
        count += 1
print(f"Sum: {sum}")
print(f"Average : {sum/count}")  '''

# Q-23)Removal of all characters from a string except integers
# Given: str1 = 'I am 25 years and 10 months old'
# Expected Output: 2510
''' num=''
str1 = 'I am 25 years and 10 months old'
for i in str1:
    if i.isdigit():
        num += i
print(num)  '''

# Q-24)Reverse words in a given String
# Input: my name is laxmi
# Output: laxmi is name my
''' txt = 'my name is laxmi'
word = txt.split()
op = " ".join(word[::-1])
print(op) '''

# Q-25)Find uncommon words from two Strings.
''' Input:  A = "apple banana mango" 
            B = "banana fruits mango"
Output:     ['apple', 'fruits'] '''

''' a = "apple banana mango" 
b = "banana fruits mango"
ab = set(a.split())
ba = set(b.split())
op = ab.symmetric_difference(ba)
print(list(sorted(op)))  '''

# Q-26)Write a program that can remove all the duplicate characters from a string. User will provide the input.
''' res =''
ip = input("Enter the string:- ")
for i in ip:
    if i not in res:
        res+=i
print(f"Result: {res}")  '''

# Q-27)Combine two lists index-wise(columns wise)
# Given List: list1 = ["M", "na", "i", "Kh"]
# list2 = ["y", "me", "s", "an"]
# Output: [['M','y'], ['na', me'], ['i', 's'], ['Kh', 'an']]
''' list1 = ["M", "na", "i", "Kh"]
list2 = ["y", "me", "s", "an"]
op = [(list1[i],list2[i]) for i in range(len(list1))]
print(op)  '''

# Q-28)Add new item to list after a specified itemWrite a program to add item 7000 after 6000 in the following Python List
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# Output: [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
'''list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)'''

# Q-29)Update no of items available
'''Input:- candy_list = ['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']
no_of_items = [10,20,34,74,32]
Output: Jelly Belly-10
        Kit Kat-20
        Double Bubble-34'''
'''candy_list = ['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']
no_of_items = [10,20,34,74,32]
for i in range(3):
    print(candy_list[i],"-",no_of_items[i])'''

# Q-30)Running Sum on list
# Input: list1 = [1,2,3,4,5,6]
# Output: [1,3,6,10,15,21]
'''list1 = [1,2,3,4,5,6]
op =[]
sum = 0
for i in list1:
    sum +=i
    op.append(sum)
print(f"Sum:- {op}")'''

# Q-31)Find list of common unique items from two list. and show in increasing order
'''Input:- num1 = [23,45,67,78,89,34]
num2 = [34,89,55,56,39,67]
Output:- [34, 67, 89]'''
'''num1 = [23,45,67,78,89,34]
num2 = [34,89,55,56,39,67] 
set_num1 = set(num1)
set_num2 = set(num2)
print(sorted(set_num1.intersection(set_num2)))'''
 
# Q-32)Convert Character Matrix to single String using string comprehension.
# Input: [['c', 'h', 'e', 't', 'a', 'n'],['s','i','r'], ['i', 's'], ['b', 'e', 's', 't'],['a'],['t', 'e', 'a', 'c', 'h', 'e', 'r']]
# Output:chetan sir is a best teacher 
'''lst = [['c', 'h', 'e', 't', 'a', 'n'],
       ['s','i','r'], ['i', 's'], ['b', 'e', 's', 't'],
       ['a'],['t', 'e', 'a', 'c', 'h', 'e', 'r']]
for i in lst:
    res = "".join(i)
    print(res,end=" ")'''
# Q-33)Add Space between Potential Words.
# Example:Input:['chetanSirIs', 'bestFor', 'dataScientist']
# Output: ['chetan Sir Is', 'best For', 'data Scientist']
'''data =  ['chetanSirIs', 'bestFor', 'dataScientist']
op =[]
for d in data:
    wrd = ''
    for i in d:
        if i.isupper():
            wrd += " " + i
        else:
            wrd +=i
    op.append(wrd.strip())    
print("Output:- ",op)'''


# Q-34)Write a program that can find the max number of each row of a matrix
# Input: [[1,2,3],[4,5,6],[7,8,9]]
# Output: [3,6,9]
'''max_ele =[]
lst = [[1,2,3],[4,5,6],[7,8,9]]
for i in lst:
    max_ele.append(max(i))
print(max_ele)'''

# Q-35)Write a list comprehension that can transpose a given matrix
'''matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]
[1, 4, 7]
[2, 5, 8]
[3, 6, 9]'''
'''matrix =  [ [1,2,3],
            [4,5,6],
            [7,8,9] ]
for i in matrix:
    print(i[0])'''


# Q-36)Join Tuples if similar initial element
# Input  : test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
# Output : [(5, 6, 7, 8), (6, 10), (7, 13)] 
'''test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
'''

# Q-38)Check is tuples are same or not?
'''t1 = (1,2,3,0)
t2 = (0,1,2,3)
if t1==t2:
    print("Tuples are same.")
else:
    print("Tuples are not same.")'''
# Alternative method.
'''t1 = (1,2,3,0)
t2 = (0,1,2,3)
x = ['same' if i in t2 else 'different'for i in t1]
if 'same' in x:
    print("Tuple is same.")
else:
    print("Tuple is not same.")'''

# Q-39)Count no of tuples, list and set from a list
# list1 = [{'hi', 'bye'},{'Geeks', 'forGeeks'},('a', 'b'),['hi', 'bye'],['a', 'b']]
# Output: List-2, Set-2, Tuples-1
'''list1 = [{'hi', 'bye'},{'Geeks', 'forGeeks'},('a', 'b'),['hi', 'bye'],['a', 'b']]
list_count = 0
tuple_count= 0
set_count=0
for i in list1:
    if type(i) == list:
        list_count +=1
    elif type(i) == set:
        set_count += 1
    elif type(i) == tuple:
        tuple_count += 1
    else:
        print("Others.")
print(f"List:-{list_count}")
print(f"Set: {set_count}")
print(f"Tuple: {tuple_count}")'''

# Q-40)Write a program to find set of common elements in three lists using sets.
# Input : ar1 = [1, 5, 10, 20, 40, 80]
#         ar2 = [6, 7, 20, 80, 100]
#         ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
# Output : [80, 20]
'''ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
set_ar1 = set(ar1)
set_ar2 = set(ar2)
set_ar3 = set(ar3)
x = set_ar1.intersection(set_ar2)
result = x.intersection(set_ar3)
print(f"Output:- {result}")'''

# Q-41)Write a program to Check if a given string is binary string of or not.
# A string is said to be binary if it's consists of only two unique characters. Take string input from user.
# Input: str = "01010101010"
# Output: Yes

# Input: str = "1222211"
# Output: Yes

# Input: str = python
# Output: No
'''s1 = input("Enter the String:- )
unique = len(set(s1))
if unique == 2:
    print("Binary String.")
else:
    print("Not Binary String.")'''

# Q-42)find union of n arrays.
# Input:
# [[1, 2, 2, 4, 3, 6],
#  [5, 1, 3, 4],
#  [9, 5, 7, 1],
#  [2, 4, 1, 3]]
# Output:
# [1, 2, 3, 4, 5, 6, 7, 9]
'''matrix = [  [1, 2, 2, 4, 3, 6],
            [5, 1, 3, 4],
            [9, 5, 7, 1],
            [2, 4, 1, 3] ]
union_set = set()
for array in matrix:
    union_set.update(array)

union_all= sorted(list(union_set))
print(union_all)'''

# Q-43)Intersection of two lists. Intersection of two list means we need to take all those elements which are common to both of the initial lists and store them into another list. Only use using list-comprehension.
# Input:  lst1 = {15, 9, 10, 56, 23, 78, 5, 4, 9}
#         lst2 = {9, 4, 5, 36, 47, 26, 10, 45, 87}
# Output: [9, 10, 4, 5]
'''lst1 = {15, 9, 10, 56, 23, 78, 5, 4, 9}
lst2 = {9, 4, 5, 36, 47, 26, 10, 45, 87}
op = list(lst1.intersection(lst2))
print(op)'''

# Q-44)Key with maximum unique values
# Given a dictionary with values list, extract key whose value has most unique values.
# Input: test_dict = {"Programmer" : [5, 7, 9, 4, 0], "is" : [6, 7, 4, 3, 3], Point: [9, 9, 6, 5, 5]}
# Output: Programmer
d = {"Programmer" : [5, 7, 9, 4, 0], "is" : [6, 7, 4, 3, 3], "Point": [9, 9, 6, 5, 5]}
prog_count = 0
is_count = 0
point_count = 0
x = (d.values())




#Q-45)Convert List to List of dictionaries. Given list values and keys list, convert these values to key value pairs in form of list of dictionaries.
# Input:  test_list = ["DataScience", 3, "is", 8]
#         key_list = ["name", "id"]
# Output: [{'name': 'DataScience', 'id': 3}, {'name': 'is', 'id': 8}]
'''test_list = ["DataScience", 3, "is", 8]
key_list = ["name", "id"]'''



# Q-46)Convert a list of Tuples into Dictionary.
# Input: [("akash", 10), ("gaurav", 12), ("anand", 14), ("suraj", 20), ("akhil", 25), ("ashish", 30)]
# Output: {'akash': [10], 'gaurav': [12], 'anand': [14], 'suraj': [20], 'akhil': [25], 'ashish': [30]}
'''lst = [("akash", 10), ("gaurav", 12), ("anand", 14), 
       ("suraj", 20), ("akhil", 25), ("ashish", 30)]
op = {k:[v] for k,v in lst}
print(op)'''

# Q-47)Sort Dictionary key and values List.
# Input: {'c': [3], 'b': [12, 10], 'a': [19, 4]}
# Output: {'a': [4, 19], 'b': [10, 12], 'c': [3]}
'''d = {'c': [3], 'b': [12, 10], 'a': [19, 4]}
op = {
    key: sorted(d[key]) for key in sorted(d)
}
print(op) '''

# Q-48)check given string is palindrome or not using string methods.
'''s = input("Enter the String for Palindrome check:- ")
rev = s[::-1]
if s == rev:
    print(f"{s} is a palindrome string.")
else:
    print(f"{s} is not a palindrome string.")'''

# Q-49)Create dictionary from the list
'''lst = [('Gaurav',3),('Anurag',4),('Rajesh',5),('Soham',6)]
op = dict(lst)
print(op)'''
# Q-50)Sort Python Dictionary by Key or Value.
'''d = {'c': [3], 'b': [12, 10], 'a': [19, 4]}
print(dict(sorted(d.items())))'''

print("----------END-----------")