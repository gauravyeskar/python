class Corse:
    def Course_det(self):
        c_id = int(input("Enter the Course Id:- "))
        c_name = input("Enter the Course Name:- ")
        c_time = int(input("Enter the Course Duration:- "))

class Department:
    def dept(self):
        d_id = int(input("Enter the Department Id:- "))
        d_name = input("Enter the Department Name:- ")

class Subject:
    def sub(self):
        s_id = int(input("Enter the Student Id:- "))
        s_name = input("Enter the Subject Name:- ")

class Faculty:
    def faclty(self):
        f_name = input("Enter the Faculty Name:- ")
        f_dept = input("Enter the Faculty Department:- ")
        f_id = int(input("Enter the Faculty Id:- "))
        f_sal = float(input("Enter the Faculty Salary:- "))
        f_mb_num = input("Enter the Mobile Number:- ")

class Exams:
    def exm(self):
        e_code = int(input("Enter the Exam Code:- "))
        e_date = input("Enter the Exam Date:- ")
        e_time = input("Enter the Exam Time:- ")
        e_room = int(input("Enter the Exam Room Number:- "))