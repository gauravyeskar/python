# program for demonstrating opening the files
# FileOpenEx1.py
try:
    fp = open("stud.data","w")
except FileNotFoundError:
    print("File doesnot Exists.")
else:
    print("\n Type of fp = ",type(fp))
    print("File Opened in Read Mode Successfully.")
