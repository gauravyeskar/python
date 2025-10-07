# Set factorial
s = int(input("Enter the size: "))
st = []
for i in range(s):
    val = int(input("Enter the value:- "))
    st.append(val)
result = []
for i in st:
    fact = 1
    for j in range(1,i+1):
        fact = fact * j
    result.append(fact)
result = set(result)
print(result)