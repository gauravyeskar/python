# program for demonstrating opening the files
# FileWithOpenEx2.py
with open("stud1.data","w") as fp:
    print("File Opened in Read Mode")
    print("Type of fp= ",type(fp))