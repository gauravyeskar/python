''' def even():
    a = int(input("Enter value to check even odd: "))
    print("Even number" if a%2==0 else "Odd number")
even() '''

def even():
    a = int(input("Enter the value: "))
    if a % 2 == 0:
        print("{} is even number. ".format(a))
    else: 
        print("{} is odd number. ".format(a))
even()