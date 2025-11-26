#The included code stub will read an integer,'n' , from STDIN.
#Without using any string methods, try to print the following:
# input:- 3      output;- 123

n = int(input("Enter number: "))
for i in range(1,n+1):
    print(i,end="")