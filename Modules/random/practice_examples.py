# Pick a random whole number between 1 and 100 (inclusive).
import random 
'''
# used for integer value.
    1.randint() --> random.randint(start,stop) --> (10-20)
    2.randrange()  --> random.randrange(start,stop-1) --> (10 - 20-1)
    -------------------
# Used for floating point value.
    1. random()  --> random.random() --> (0.0 to 1.0) values
    2. uniform() --> random.uniform() --> (10 to 20) values
    -------------------
    5. choice() --> random.choice(iterable_obj)
    6. shuffle() --> random.shuffle(iterable_obj) shuffles the values of mutable type
    7. sample() --> random.sample(iterable_obj,K=num. of samples)
    --------------------
'''
#print(random.randrange(1,101))
#print(dir(random))
# Simulate a dice roll by getting a random number between 1 and 6.
#print(random.randint(1,6))

# Create a random decimal number between 0.0 and 1.0.
#a = random.random()
#print(a)

# Generate a random decimal number between 50 and 100.
#b = random.uniform(50,100)
#print(b)

# Select a random day of the week from a list: ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'].
#l = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']
#print(random.choice(l))

# Randomly pick a winner from a list of participant names.
#l = ['Gaurav','Shiu','Sayali','Rohan','kapil','Rajesh']
#print(random.choice(l))

# Write a program that randomly prints either "Heads" or "Tails".
# l = ['Heads','Tails']
# print(random.choice(l))

# Given a list of numbers from 1 to 52, use random.shuffle() to randomize their order.
# n = list(range(1,53))
# random.shuffle(n)
# print(n)

# Challenge: Create a list of card objects (e.g., {'suit': 'Hearts', 'rank': 'A'}) and shuffle them.
#l = ['suit','Hearts','rank','B','color','black','Sports','Football']
#print(random.shuffle(l))

# s = 'PYTHON'
# lst = random.sample(s,3)
# print(lst)

# Create a 12-character password that includes a mix of uppercase letters, lowercase letters, digits, and special characters.
#  You can use random.choice() in a loop to build the string.


# Randomly select 6 unique numbers from 1 to 49 for a lottery ticket.
print(random.sample(range(1,49),6))

# With sample() create number plate.
'''state = ['MH','MP','GJ','RJ','DD']
rtocode = ['01','02','03','04','05','06','07','08']
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = "0123456789"
for i in range(1,10):
    st1 = random.sample(state,1)
    rto = random.sample(rtocode,1)
    alpha = random.sample(alpha,2)
    no = random.sample(nums,4)
    sst1 = ""
    sst1 = sst1.join(st1)
    srto = ""
    srto = srto.join(rto)
    salpha = ""
    salpha = salpha.join(alpha)
    sno = ""
    sno = sno.join(no)
    number_plate = sst1+" " + srto+" " + salpha+" " + sno
    print(number_plate)'''