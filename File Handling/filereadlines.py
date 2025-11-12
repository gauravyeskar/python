# readlines():- It is used to read entire/complete file data from file in the form of list.
#  syn:        varname = filepointer.readlines()

with open("fathers.txt","r") as fp:
    filedata= fp.readlines()
    print("*"*20)
    for fd in filedata:
        print(fd)
    print(type(filedata))