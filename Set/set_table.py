# set table

s = int(input("Enter the size: "))
st = set()
for i in range(s):
    val = int(input("Enter the value:- "))
    st.add(val)
for i in st:
    for j in range(1,11):
        print("{} * {} = {}".format(i,j,i*j))
    print("*-*"*8)
    print()