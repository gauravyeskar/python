# Entering the data from keyboard.
with open("Dynamic.txt",'a') as fp:
    print("Enter the data or Press @ to stop: ")
    while(True):
        kdata = input()
        if(kdata) !='@':
            fp.write(kdata +'\n')
        else:
            break
    print("Data Written..!!")


