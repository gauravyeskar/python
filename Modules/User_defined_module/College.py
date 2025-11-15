# W.A.P.P. which will implement the following
# Let's assume there exist a university which contains University name and location. Accept and display university details. 
# Let's assume there exists a college which contains college name and location. Accept and display college details along with university details.
# Let's assume there exists a student which contains student number, name and course. Accept and display std details along with college and university details
from University import University
class College(University):
    def getclgdetails(self):
        self.cname = input("Enter the College name:- ")
        self.cloca = input("Enter the College Location:- ")
    def dispClgDetails(self):
        print("-"*50)
        print("----------COLLEGE DETAILS----------")
        print(f"College Name: {self.cname}\nCollege location:  {self.cloca}.")
        print("-"*50)