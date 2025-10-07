# Armstrong Dict
d = {}
s = int(input("Enter the size: "))
for j in range(s):
    name = input("Enter the name of dictionary: ")
    value = int(input("Enter the value for name: "))
    d[name] = value
print("*"*20)
d.values()
arm_count = 0
no_arm_count = 0
arm_number = []
no_arm_number = []
for i in d.values():
    t = i
    t1 = i
    length = 0
    while(i>0):
        length +=1
        i //= 10
    armstrong = 0
    while(t>0):
        ld = t % 10
        armstrong = armstrong +(ld ** length)
        t //= 10
    if(t1 == armstrong):
        arm_count +=1
        arm_number.append(t1)
        print("{} is armstrong number.".format(t1))
    else:
        no_arm_count += 1
        no_arm_number.append(t1)
        print("{} is not a armstrong number.".format(t1))
print("*"*20)
print("Armstrong count is: ",arm_count)
print("Armstrong numbers are: ",arm_number)
print("Not Armstrong count is: ",no_arm_count)
print("Not Armstrong Numbers are: ",no_arm_number)
print("*"*20)