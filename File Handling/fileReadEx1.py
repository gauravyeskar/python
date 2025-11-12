# read():- It is used for reading the entire/ complete file data from the file.
#  syn:        varname = filepointer.read()

with open("Addr1.txt","r") as fp:
    filedata= fp.read()
    print("*"*20)
    print(filedata)