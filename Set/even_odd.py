# Even odd set 

s = int(input("Enter the size:- "))
st = set()
even_count = 0
odd_count = 0
even_st = set()
odd_st = set()
for i in range(0,s):
    val = int(input("Enter the value:- "))
    st.add(val)
for j in st:
    if j%2 == 0:
        even_st.add(j)
        even_count += 1
        print("{} is even number".format(j))
    else: 
        odd_st.add(j)
        odd_count += 1
        print("{} is odd number".format(j))
print("*"*30)
print("Even set is: ",even_st)
print("Total even count is:- ",even_count)
print("Odd set is: ",odd_st)
print("Total odd count is:- ",odd_count)