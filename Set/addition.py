# Set Addition
s = int(input("Enter the size:- "))
st = set()
for i in range(s):
    val = int(input("Enter the value:- "))
    st.add(val)
sum = 0
count = 0
length = 0
for i in st:
    count +=1
for j in st:
    sum +=j
    length +=1
    if(length < count):
        print("{} + ".format(j),end= "")
    else: 
        print("{} = ".format(j),sum)