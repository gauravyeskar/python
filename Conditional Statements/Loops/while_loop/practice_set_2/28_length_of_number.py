n=int(input("Enter the number: "))
len=0
while(n>0):
    len+=1
    lst_dig=n%10
    n=n//10
print(f"The length of number is {len} digit.")