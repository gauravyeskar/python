# Armstrong list
s = int(input("Enter size of list:"))
L = []
yes_armstrong = 0
no_armstrong = 0
arm_num = []
no_arm_num = []
for i in range(s):
    val = int(input("Enter the value: "))
    L.append(val)
print(L)
for i in L:
    t = i
    t1 = i
    length = 0
    while(i>0):
        length +=1
        i//=10
    armstrong = 0

    while(t > 0):
        last_digit = t%10
        armstrong = armstrong +(last_digit ** length)
        t //= 10
    if(t1 == armstrong):
        arm_num.append(t1)
        yes_armstrong +=1
        print(t1," is a Armstrong number.")
    else:
        no_armstrong +=1
        no_arm_num.append(t1)
        print(t1," is not a Armstrong Number.")
print("Total count of Armstrong Number:- ",yes_armstrong)
print("Armstrong numbers are: ",arm_num)
print("Total count of Non-Armstrong Number:- ",no_armstrong)
print("Non armstrong numbers are: ",no_arm_num)