# Tuple AArmstrong
s = int(input("Enter the size: "))
t = ()
arm_count = 0
no_arm_count = 0
for i in range(0,s):
    val = int(input("Enter the values: "))
    t = list(t)
    t.append(val)
for j in t:
    l = j
    l1 = j
    count = 0
    while(j>0):
        count +=1
        j //=10
    armstrong = 0
    while(l > 0):
        ld = l % 10
        armstrong = armstrong +(ld ** count)
        l //= 10
    if(armstrong == l1):
        arm_count +=1
        print(l1,"armstrong")
    else:
        no_arm_count +=1
        print(l1,"not armstrong Number.")
print("*"*20)
print(no_arm_count," is No armstrong number count.")
print(arm_count," Armstrong number count.")
print("*"*20)