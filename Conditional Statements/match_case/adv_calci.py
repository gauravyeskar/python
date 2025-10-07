a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("*"*20)
c = input("Enter the operation your want to do: ")
print("*"*20)

match(c):
    case '+':
        print("Your addition is: ",a+b)
        print("*"*20) 
    case '-':
        print("Your substraction is: ",a-b)
        print("*"*20)
    case '*':
        print("Your multiplication is: ",a*b)
        print("*"*20)
    case '/':
        print("Your division is: ",a/b)
        print("*"*20)
    case '//':
        print("Your floor division operation is: ",a//b)
        print("*"*20)
    case '%':
        print("Your modulous operation is: ",a%b)
        print("*"*20)
    case '==':
        print("Your values are equal: ",a==b)
        print("*"*20)
    case '<=':
        print("Your first value is less than second: ",a<=b)
        print("*"*20)
    case '>=':
        print("Your first value is greater than second value: ",a>=b)
        print("*"*20)
    case '!=':
        print("Your values are not equal: ",a!=b)
        print("*"*20)
    case '&':
        print("Your AND operator is True: ",a&b)
        print("*"*20)
    case '|':
        print("Your Or operator is True: ",a|b)
        print("*"*20)
    case '~':
        print("Your NOT operator is True: ",~a)
        print("*"*20)
    case '^':
        print("Your XOR is True:",a^b)
    case __:
        print("Invalid Choice.")
        print("*"*20)
    