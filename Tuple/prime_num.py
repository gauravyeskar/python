# Prime list
s = int(input("Enter the size: "))
t = ()
prime_ct = 0
non_prime_ct = 0
prime_tup = ()
non_prime_tup = ()
for i in range(s):
    val = int(input("Enter the values: "))
    t = list(t)
    t.append(val)

for j in t:
    if(j>0):
        prime = True
        for i in range(2,j):
            if(j%i == 0):
                prime = False
                break
        if(prime):
            prime_ct += 1
            prime_tup = list(prime_tup)
            prime_tup.append(j)
            print("{} is a prime number.".format(j))
        else:
            non_prime_ct += 1
            non_prime_tup = list(non_prime_tup)
            non_prime_tup.append(j)
            print("{} is not a prime number.".format(j))
    else:
        non_prime_ct += 1
        non_prime_tup = list(non_prime_tup)
        non_prime_tup.append(j)
        print("Not Prime Number.")
print("*"*20)
print("Total prime count is: ",prime_ct) 
print("Total Non-prime count is: ",non_prime_ct)
print("*"*20)
non_prime_tup = tuple(non_prime_tup)
prime_tup = tuple(prime_tup)
print("All prime numbers are: ",prime_tup)
print("All Non Prime numbers are: ",non_prime_tup)
print("*"*20)