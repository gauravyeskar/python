# W.A.P.P. which will implement the following
# Let's assume there exist a university which contains University name and location. Accept and display university details. 
# Let's assume there exists a college which contains college name and location. Accept and display college details along with university details.
# Let's assume there exists a student which contains student number, name and course. Accept and display std details along with college and university details.
class University:
    def getunivdetails(self):
        self.uname = input("Enter the University name:- ")
        self.uloca = input("Enter the University Location:- ")
    def dispUniDetails(self):
        print("-"*50)
        print("----------UNIVERSITY DETAILS----------")
        print(f"University Name: {self.uname}\nUniversity location:  {self.uloca}.")
        print("-"*50)
class College(University):
    def getclgdetails(self):
        self.cname = input("Enter the College name:- ")
        self.cloca = input("Enter the College Location:- ")
    def dispClgDetails(self):
        print("-"*50)
        print("----------COLLEGE DETAILS----------")
        print(f"College Name: {self.cname}\nCollege location:  {self.cloca}.")
        print("-"*50)
class Student(College):
    def getStddetails(self):
        self.sID = input("Enter the Student number:- ")
        self.sname = input("Enter the Student name:- ")
        self.scourse = input("Enter the Student Course:- ")
    def dispStdDetails(self):
        print("-"*50)
        print("----------STUDENT DETAILS----------")
        print(f"Student ID: {self.sID}\nStudent Name: {self.sname}\nStudent location:  {self.scourse}.")
        print("-"*50)
# Main Program
so = Student()
so.getStddetails()
so.getclgdetails()
so.getunivdetails()
so.dispStdDetails()
so.dispClgDetails()
so.dispUniDetails()