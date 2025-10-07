print("*"*60)
print("For addition press 1")
print("For substraction press 2")
print("For multiplication press 3")
print("For division press 4")
print("*"*60)
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("*"*20)

c= str(input("Enter your choice: "))
print("*"*60)
match(c):
    case '1':
        print("The addition of",a,'+',b,"=",a+b )
        print("*"*60)
    case '2':
        print("The substraction of",a,'-',b,"=",a-b)
        print("*"*60)
    case '3':
        print("The multiplication of",a,'*',b,'=',a*b)
        print("*"*60)
    case '4':
        print("The division of",a,'/',b,'=',a/b)
        print("*"*60)
    case __:
        print("Invalid choice..")
        print("*"*60)