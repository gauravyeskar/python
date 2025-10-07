sp = 1
ep = 11
sum = 0
for sp in range(sp,ep,1):
    if(sp<(ep-1)):
        print(sp,"+", end=" ")
        sum +=sp
    else: 
        print(sp,"=",end=" ")
        sum += sp
print(sum)