char = input("Enter the character: ")
match(char):
    case _ if char in ('a','e','i','o','u'):
        print("Lower Vowel.")
    case _ if char in ('A','E','I','O','U'):
        print("Upper Vowel.")
    case _ if(char == 'b','c','d','f','g','h','j','k','l','m','n',
              'p','q','r','s','t','v','w','x','y','z'):
        print("Lower Consonant")
    case _ if(char == 'B','C','D','F','G','H','J','K','L','M','N',
              'P','Q','R','S','T','V','W','X','Y','Z'):
        print("Upper consonant")
    case __:
        print("Invalid Input")