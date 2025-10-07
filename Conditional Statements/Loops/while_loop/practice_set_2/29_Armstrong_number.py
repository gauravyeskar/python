# Check armstrong number
n = int(input("Enter the number: "))
num = n
len=0
while(n>0):
    len+=1
    ld = n%10
    n//=10
print(f"The length is {len} digits.")
print("*"*20)

if(len == 1):
    one = num % 10
    arm = one**len
else:
    if(len == 2):
        two= (num//10)%10
        one= num%10
        arm= (two**len)+(one**len)

    if(len == 3):
        three=(num//100)%10
        two= (num//10)%10
        one= num%10
        arm= (three**len)+(two**len)+(one**len)
      
    if(len == 4):
        four = (num//1000)%10
        three=(num//100)%10
        two= (num//10)%10
        one= num%10
        arm= (four**len)+(three**len)+(two**len)+(one**len)
if num == arm:
    print("Armstrong number.")
    print(num,"=",arm)
else: 
    print("Not armstrong number.")   