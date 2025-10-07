# A small hands on try on all of the special functions.

import functools
print("Enter list of salaries of Employees :- ")
sallist = [float(sal) for sal in input().split() if float(sal) > 0 and float(sal) <= 1000]
print("*"*50)
print("Given salary List = ",sallist)
print("*"*50)

# Filter the salaries range from 0 to 500
sal_0_500 = list(filter(lambda sal : 0<=sal <= 500,sallist))

# Filter the salaries range from 501 to 1000
sal_501_1000 = list(filter(lambda sal: 501<=sal <=1000,sallist))

# Give hike 10% for those employee range 0 to 500
hike_sal_0_500 = list(map(lambda sal: sal + sal+ sal * 10/100,sal_0_500))

# Give hike 10% for those employee range 501 to 1000
hike_sal_501_1000 = list(map(lambda sal: sal + sal *20/100,sal_501_1000))

# Find total salary of 0 to 500
total_sal_0_500 = functools.reduce(lambda sal1,sal2:sal1+sal2,sal_0_500)

# Find total salary of 0 to 500 after hike
tothikesal_0_500 = functools.reduce(lambda sal1,sal2:sal1+sal2,hike_sal_0_500)

# Find total salary of 501 to 1000
totsal_501_1000 = functools.reduce(lambda sal1,sal2:sal1+sal2,sal_501_1000)

#find total salary of 501 to 1000 after hike
tothikesal_501_1000 = functools.reduce(lambda sal1,sal2:sal1+sal2,hike_sal_501_1000)

print("="*50)
print("Old salary 0-500    Hike_Sal 0-500")
print("="*50)
print("      {}                   {}".format(total_sal_0_500,tothikesal_0_500))
print("="*50)
print("Old salary 501     Hike_Sal 501-1000")
print("="*50)
for asal,nsal in zip(sal_501_1000,hike_sal_501_1000):
    print("  {}                   {}".format(asal,nsal))
print("="*50)
print("{}                         {} ".format(totsal_501_1000,tothikesal_501_1000))
print("*"*50)
print("*"*50)