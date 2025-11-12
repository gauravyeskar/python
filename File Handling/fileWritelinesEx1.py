# Program writing the data to the file
x = [10,"Rossum","Python","Data Science",True]
with open("Fathers.txt","w") as fp:
    fp.writelines(str(x)+"\n")
    print("Data Written...!!")


x = [20,"Kinney","pandas","Data Analyst"]
with open("Fathers.txt","a") as fp:
    fp.writelines(str(x)+ "\n")
    print("Data Written...!!")


x = {30,"Ritche","C"}
with open("Fathers.txt","a") as fp:
    fp.writelines(str(x)+"\n")
    print("Data Written...!!")

x = {10:'C',20:'C++',30:'Python',40:'java'}
with open("Fathers.txt","a") as fp:
    fp.writelines(str(x)+"\n")
    print("Data Written...!!")