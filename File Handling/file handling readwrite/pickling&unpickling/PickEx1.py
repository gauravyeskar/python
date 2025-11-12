# Pickling:- Used to load the data into the file from iterable object at once. It uses dump() to save the data into the file with single write operation.
# UnPickling:- Used to retrive whole data from the file at once. It uses load() to retrieve data with single read operation. .
# NOTE:- The dump() (write) and load() (read) always takes the file in binary format.
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# W.A.P.P. which will write the student data from the keyboard and save as a record in a file.(pickling)
import pickle as p
def saverecord():
    with open('stud.txt','ab') as fp:
        print("-"*20)
        no = int(input("Enter Student Number:- "))
        name = input("Enter Student Name:- ")
        marks = float(input("Enter the Marks:- "))
        l = []
        l = l.append(no),l.append(name),l.append(marks)
        p.dump(l,fp)
        print("-"*20)
        print("Record Saved Successfully...!!")
        print("-"*20)
        ch = input(("Do You Want to insert more data..(yes/no):- "))
        if ch.lower() == 'no':
            print("Thanks For Using my Application.")
            print("-"*30)
            breakpoint
        else:
            saverecord()
            print("="*25)
saverecord()