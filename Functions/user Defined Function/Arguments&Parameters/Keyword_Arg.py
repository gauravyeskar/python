'''   KEYWORD ARGUMENT:- 
1. In some cases we know the key name and value but we dont know the value of it at that time it is used.
2. It is just like the dictionary in the form of key value pairs.
3. It will return class as function.

Syn:-
        def fun_nm(key1,key2):
                code
                code
                code
        fun_nm(key1 = val1, key2 = val2)
'''

def add(b,a,e=20):
    c = a + b + e
    return c 
d = add(a = 10, b = 20)
print("The output is: ",d)

def disp(a,b,c,d):
    print("\t {} \t {} \t {} \t {}".format(a,b,c,d))
    print("\t","*"*26)

disp(10,20,30,40)
print("Display:- ",disp,type(disp))