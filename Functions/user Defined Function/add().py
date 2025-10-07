"""def add():
    '''I am doc string'''
    a = 10
    b = 20
    c = a+b
    print("The Output without returning is:- ",c)
add() """

'''
def ad():
    a = 10
    b = 20
    c = a+b
    return c
addd = ad()
print("The result after returning C is: ",addd)
'''

'''
def add():
    a = 10
    b = 20
    c = a + b
    return a,b,c
x,y,z = add()
print("Result after Returning multiple variables: ",x,y,z)
'''

def add():
    a = int(input("Enter the first value: "))
    b = int(input("Enter the second value: "))
    c = a + b
    return c
print("The result is: ",add())