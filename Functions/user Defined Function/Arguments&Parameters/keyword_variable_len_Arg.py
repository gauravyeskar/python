''' Keyword variable length argument
1. When we have multiple call keyword with key word variable number of values/ arguments we use this argument type..
2. just like dicionary but also having variables with it.
3. Its type will be < 'dict' >
Syn:-   
        def fun_nm(list of formal para, **val):
                    code
                    code
                    code
        fun_nm(arg1,arg2...,arg n)
'''

def add(**val):
    print(val)
add(a = 10 , b = 20)

def disp(**val):
    print("*"*20)
    for i,j in val.items():
        print("\t{} --> {}".format(i,j))
    print("-"*20)

disp(eno = 10,ename = "GSY",sal = 34.250,cname="TCS")