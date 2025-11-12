# program for demonstrating opening the files
# FileWithOpenEx1.py
try:
    with open("stud1.data") as fp:
        print("File Opened in Read Mode")
        print("Type of fp= ",type(fp))
except FileNotFoundError:
    print("File Deos not exists")
