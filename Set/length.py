# Length set 

s = int(input("Enter the size:- "))
st = set()
count = 0
for i in range(0,s):
    val = int(input("Enter the value:- "))
    st.add(val)
    count += 1
print("*"*10)
print("Elements of sets are: ", st)
print("Total count is:- ",count)