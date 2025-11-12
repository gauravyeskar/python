# Checking the Number is prime or not

n = int(input("Enter the number:- "))
def prime():
    if n < 0:
        print("{} is invalid Number.".format(n))
    else:
        result = 'Prime'
        for i in range(2,n):
            if n%i == 0:
                result = 'Not Prime'
        if result == 'Prime':
            print("{} is {}".format(n,result))
        else:
            print("{} is {}".format(n,result))
