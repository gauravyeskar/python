'''
# Default Arguments:- 
1. It is used when the value of the argument is static or constant then we have to pass that value at the last index value of the parameter 
    by assigning the value.
2. if not we get syntax error.
3. If we assign the default variable and we are passing the value of that static variable then the new value is taken in place of the default. 

Syn:-
        def fun_nm(par1,par2 = default_val):
                code 
                code
                code
        fun_nm(arg1) #NO NEED OF ARG2
'''

def add(a,b=20): # b = 20 is default variable.
    c = a + b
    return c
d = add(10)   # passed value of a.
print("Output is: ",d)


def sub(a, b=10): # Statis value over ride
    c = a-b
    return c
d = sub(20,40)
print("Substraction is: ",d,type(d))