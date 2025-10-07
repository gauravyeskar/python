day_num = int(input("Enter the day number: "))
match(day_num):
    case 1:
        print("monday")
        print("*" * 30)
    case 2:
        print("Tuesday")
        print("*" * 30)
    case 3:
        print("Wednesday")
        print("*" * 30)
    case 4:
        print("Thursday")
        print("*" * 30)
    case 5:
        print("Friday")
        print("*" * 30)
    case 6:
        print("Saturday")
        print("*" * 30)
    case 7:
        print("Sunday")
        print("*" * 30)
    case __:
        print("Invalid")
        print("*" * 30)