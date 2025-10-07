'''
1. It is the basic or default function.
2. Every argument passing to every formal parameters based in their position by maintaining order and meaning for higher accuracy.
3. The number of arguments are equal o the number of paramenters.
4. It is used for passing the values for function call to function defination.
5. PVM gives higher priority to Positional Argument.

# Syn:- 
            def fun_name(parameter1, par2,par3):
                code
                code
                code
            fun_name(arg1,arg2,arg3)
 
'''

def add(a,b): # Parameters
    c= a + b 
    return c
d=add(10,20)  #arguments 
print("The output is: ",d,type(d))