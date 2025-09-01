# FUNCTIONS IN PYTHON STRING.
# .capitalize:- Make capital first letter of first word in string .
print("*"*30)
#print(dir(str))
s= 'gaurav santosh yeskar'
s=s.capitalize()
print(s) # Gaurav santosh yeskar

# .title:- Make capital every word's first letter in string.
s= 'gaurav santosh yeskar'
s=s.title()
print(s)  # Gaurav Santosh Yeskar

# .index:- Returns index value passed in ('...') .
s= 'gaurav santosh yeskar'
s=s.index('s')
print(s)

# .upper:- returns string in uppercase.
s= 'gaurav santosh yeskar'
s=s.upper()
print(s)  # GAURAV SANTOSH YESKAR

# .lower:- Returns string to lowercase.
s= 'GAURAV SANTOSH YESKAR'
s=s.lower()
print(s)  #gaurav santosh yeskar

# .isupper:- Checks that whether all string is in uppercase or not and returns boolean value.
s= 'GAURAV SANTOSH YESKAR'
s=s.isupper()
print(s) #True

# .islower:- Checks that whether all string is in lowercase or not and returns boolean value.
s= 'gaurav santosh yeskar'
s=s.islower()
print(s) #True

s= 'Gaurav santosh yeskar'
s=s.islower()
print(s)  #False

# .isdigit:- Checks that whether all string contains digits or not and returns boolean value.
s= '123456789'
s=s.isdigit()
print(s) #True

s= 'Hello World123'
s=s.isdigit()
print(s) #False

# .isalpha:- Checks that whether the first letter of string is in upper or not and returns boolean value.
s= 'Hello'
s=s.isalpha()
print(s) #True

s= 'Hello World'
s=s.isalpha()
print(s) #False becz of space.

# .isalnum:- Checks that whether the string contains alphabet and digits both or not and returns boolean value.
s= 'hello123'
s=s.isalnum()
print(s) #True

s= 'hello@123'
s=s.isalnum()
print(s) #False bcz of '@'.

# .isspace:- Checks that whether there is only space in string or not and returns boolean value.
s= ' '
s=s.isspace()
print(s) #True

s= ' hello'
s=s.isspace()
print(s) #False It only takes space.

# .split():- Splits the string in elements of list..
s= 'Hello Python'
s=s.split()
print(s)  #['Hello', 'Python']

s= 'Hello-Python'
s=s.split("-")
print(s)  # Hello Python 

# .join():- It joins both strings.
words = ["Python", "is", "fun"]
result = " ".join(words)
print(result)  #Python is fun

# .startswith():- Checks that whether the string starts with the value passed in ('....') or not and returns boolean value.
s= 'Hello Python'
s=s.startswith('Hello')
print(s)  #True

s= 'Hello Python'
s=s.startswith('Helo')
print(s)  #False

# .endswith():- Checks that whether the string ends with the value passed in ('....') or not and returns boolean value.
s= 'Hello Python'
s=s.endswith('python')
print(s)  #True

s= 'Hello Python'
s=s.endswith('Hello')
print(s)  #False

# .swapcase():- It will swap the capital letters to small letters and vice-versa.
s= 'Hello Python'
s=s.swapcase()
print(s)  #hELLO pYTHON (capital to small letters and vice-versa.)

# .isnumeric():- checks whether the string contains Unicode characters that represent numbers, including fractions, 
#                Roman numerals, and other numeric symbols.
#.isdigit():- checks only for digits.
#.isnumeric():- checks for digits and for expressions contained or not in string.

s= '123'
print(s.isnumeric())  # True

s= '123a'
print(s.isnumeric())  # False

s= '1/2'
print(s.isnumeric())  # True

s="½".isnumeric()
print(s) #True

#.isdigits():- checks for base-10 decimal digits (0-9).
s='123456'
print(s.isdecimal())  #True

# .isascii():- It will check whether string have Unicode code points within the ASCII range (0-127), and False otherwise.
s= 'Hello Python'.isascii()
print(s)

s= 'Hello Python123'.isascii()
print(s)

#.maketrans():- Will change the letter given in("to be changed","with letter")
s = 'Hello Sam'
s1 = s.maketrans("S","P")
print(s.translate(s1)) #Hello Pam

#.find():- returns index value
s = 'Python sql java'
print(s.find("sql"))  # 7

s = 'Python sql java'
print(s.find("shiva"))  # -1. bcz not present in it.

#.replace():- It replaces the word in the strings. 
s= 'Hello Python'
print(s.replace("Python","Java"))  #Hello Java

#.strip():- It removes the space from before and after. 
s= ' Hello '
print(s.strip()) #Hello

#.rstrip():- It removes the space from right. 
s= ' Hello '
print(s.rstrip()) # Hello

#.lstrip():- It removes the space from left. 
s= ' Hello '
print(s.lstrip()) #Hello

#.count():- Counts the occurance of the letter mentioned ("...").
s = 'hello'
print(s.count('l')) # 2

#.center():- Takes the string in the center(total chars,"symbol")
s = 'Hello'
print(s.center(11,'*')) # ***Hello***

#.casefold():- returns into lowercase.
s = 'Hello'
print(s.casefold()) # hello

#.partition():- returns into tuple.
s = 'python sql java'
print(s.partition('sql')) #('python ', 'sql', ' java')

#.translate():-  
s ={83 : 80}
t = 'Hello world'
print(t.translate(s))

#.expandtabs() :- 
s='g\ta\tu\tr\ta\tv'
print(s.expandtabs(2)) # g  a  u  r  a  v

#.format():-
s= 'for only {price: .2f} dollars'
print(s.format(price = 49)) # for only  49.00 dollars

#.format_map():- 
s = {"name" : "Sam", "age" : 25}
t = "Happy birthday {name} you are now on level {age}!"
print(t.format_map(s)) #Happy birthday Sam you are now on level 25!

#print(help(str(format))) # Used to see why the specified method is used.
print(dir(str))