# Program to writing the data to the file.
with open("Addr1.txt","w") as fp:
    fp.write("100\n")
    fp.write("Gaurav\n")
    fp.write("11.11\n")
    fp.write("*******************")
    print("data return to the file")

with open("Addr1.txt","a") as fp:
    fp.write("200\n")
    fp.write("Sonu\n")
    fp.write("34.11\n")
    print("data return to the file")