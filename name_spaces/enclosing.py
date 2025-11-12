a = 10
def f1():
    b=20
    def f2():
        c = a + b
        print(a)
        print(b)
        print(c)
    f2()
f1()