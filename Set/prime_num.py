# Prime set 

s = int(input("Enter the size:- "))
st = set()
prime_ct = 0
no_prime = 0
prime_set = set()
non_prime_set = set()
for i in range(s):
    val = int(input("Enter the value:- "))
    st.add(val)
for j in st:
    if(j > 0):
        prime = True
        for i in range(2,j):
            if j % i == 0:
                prime = False
                break
        if prime:
            prime_ct += 1
            prime_set.add(j)
            print("Prime number.")
        else:
            no_prime += 1
            non_prime_set.add(j)
            print("Not prime Number.")
    else:
        no_prime += 1
        non_prime_set.add(j)
        print("Not prime number.")
print("*"*30)
print("Total prime number count is: ",prime_ct)
print("Total non prime number count is: ",no_prime)
print("*"*30)
print("Prime numbers are: ", prime_set)
print("Non prime numbers are: ",non_prime_set)
print("*"*30)