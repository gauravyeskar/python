a = 10
b = 20
c = 30
d = 40
def operation():
    a = 100
    b = 200
    c = 300
    d = 400
    simple_result = a+b+c+d
    print(simple_result,"  From local variable.")
    global_result = a+b+c+d+globals()['a']+globals().get('b')+globals()['c']+globals()['d']
    print(global_result," Result form globals")


operation()