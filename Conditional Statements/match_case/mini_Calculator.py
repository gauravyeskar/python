a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))
print("*" * 30)
c = input("Enter which operation you want to perform: '+' , '-' , '*' , '/' :- ")
print("*" * 30)
match(c):
    case '+':
        print("Your addition is: ",a+b)
    case '-':
        print("Your substraction is: ",a-b)
    case '*':
        print("Your multiplication is: ",a*b)
    case '/':
        print("Your division is: ",a/b)
    case __:
        print("Default Input")