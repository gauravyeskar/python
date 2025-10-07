print("Sum of 1 to 10")
i = 1
sum = 1
while(i<=10):
    if(i<10):
        print(i,"+ ",end="")
    else:
        print(i,"= ",sum,end="")
    i+=1
    sum+=i