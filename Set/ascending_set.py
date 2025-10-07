#Ascending set 

s = int(input("Enter the size:- "))
st = []
for i in range(s):
    val = int(input("Enter the value:- "))
    st.append(val)
for j in range(0,s):
    for k in range(j+1,s):
        if(st[j]>st[k]):
            st[j],st[k] = st[k],st[j]
st = tuple(st)
print("Ascending set is: ",st)