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