'''  VARIABLE LENGTH
1. When we have multiple function calls with variable function value then with the normal arguments its will not happen
2. for it we have to take variable length variable (*variable_name).
3. It's type will be tuple.

## Rule1 :-
            variable name should be 1 not more are placed at the last.
    Rule2 :-

Syn:- 
        def fun_nm(*val):
            code
            code
            code
        fun_nm(val1,val2,val3,val4,val5,val6,...,valn-1)
'''

def add(*val):
    print(val,type(val))
add(10,20,30,40,50,60,70,80,90)


def disp(sno,sname,*vals):
    print("*"*20)
    print("Student number: {}".format(sno))
    print("Student name: {}".format(sname))
    s = 0
    for val in vals:
        print("{} ".format(val),end = " ")
        s = s + val
    print()
    print("Sum = {}".format(s))
    print("*"*20)
disp(101,"Gaurav",10,20,30,40,50)
disp(102,"Sonu",50,40,30,20,10)
disp(103,"Dennis",90,99,98,95,99)
disp(104,"Priya",50,40,60,20,10)