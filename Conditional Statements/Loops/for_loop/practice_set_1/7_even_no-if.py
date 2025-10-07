start = int(input("Enter the starting point: ")) #1
end = int(input("Enter the ending point: ")) #10
start+=start%2  #11
temp = start
for temp in range(start,end+1,2):
    print(temp)