# Prime number

s = int(input("Enter the Size: "))  #5
l = []
prime_count = 0
prime_list = []
not_prime_count = 0
not_prime_list = []
for k in range(0,s):
    val = int(input("Enter the value: "))
    l.append(val)
print(l) 
for j in l:
    if j > 1:
        is_prime = True
        for i in range(2,s+1): #(2,6)
            if(j%i == 0):
                is_prime = False
                break
            if is_prime:
                prime_count +=1
                prime_list.append(i)
                print(i,"is prime number.")
            else:
                not_prime_count +=1
                not_prime_list.append(i)
                print(i,"is not prime number.")
    else:
        print("Number should be greater than 1.")

print("*"*40)
print("Total prime count: ",prime_count)
print("Prime list: ",prime_list)
print("*"*40)
print("Total not prime count: ",not_prime_count)
print("Total not prime list: ",not_prime_list)
print("*"*40)