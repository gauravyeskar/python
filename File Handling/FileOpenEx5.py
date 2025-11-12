#W.A.P.T.which will obtain internal information about the files such as file name, file mode,readability,writability,closability.
# FileOpenEx5.py
with open("stud2.data","w") as fp:
    print("*"*20)
    print("File Opened in Write Mode")
    print("*"*20)
    print("File Name: ",fp.name)
    print("File Opening Mode: ",fp.mode)
    print("Is this file Readable: ",fp.readable())
    print("Is this file writable: ",fp.writable())
    print("Is this file closed: ",fp.closed)
    print("*"*20)
print("Out of With Open() as")
print("Is this file closed: ",fp.closed)
