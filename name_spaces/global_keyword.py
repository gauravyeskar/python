# Modifying global variable using global keyword

a = 10
def opps():
    global a 
    a+=1
    print("a is a global modifying variable so needs to use global keyword.")
    print(a)

opps()
print("*"*50)

b = 20
def h():
    print("No global Example: ")
    print("-"*20)
    k = b + 10
    print("K is assigned variable. so no need to use global keyword.")
    print(k)

h()