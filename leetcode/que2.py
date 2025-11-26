# rite a program that reads an integer 'n' from user. For all negative integers i<n, prints square of 'i'
'''n = int(input("Enter the number:- "))
for i in range(n):
    print(i*i)'''


# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.
def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    
    return leap

year = int(input("Enter Year:-"))
print(is_leap(year))