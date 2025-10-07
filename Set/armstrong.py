# Set Armstrong

s = int(input("Enter the size:- "))
st = set()
yes_strong = 0
no_strong = 0
for i in range(s):
    val = int(input("Enter the value:- "))
    st.add(val)
for j in st:
    t = j
    t1 = j 
    length = 0
    while(j > 0):
        length +=1
        j //= 10 
        armstrong = 0
        while(t > 0):
            ld = t % 10
            armstrong = armstrong + (ld ** length)
            t //= 10
    if(t1 == armstrong):
        yes_strong += 1
        print("{} is armstrong number".format(t1))
    else:
        no_strong += 1
        print("{} is not an armstrong number.".format(t1))
print("Total count of Armstrong Number:- ",yes_strong)
print("Total count of Non-Armstrong Number:- ",no_strong)