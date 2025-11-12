# Book Library: Create a Book class. The constructor must take 
# title and author. Add an instance attribute is_checked_out and
# initialize it to False.

class Book:
    def __init__(self,author,title):
        self.title = title
        self.author = author
    def show_data(self):
        print(f"The Book is {self.title} and Written by {self.author}")


author = input("Enter the Author's Name:- ") 
title = input("Enter the Book Title:- ")
b1 = Book(author,title)
print(b1.is_checked_out())
print(b1.show_data())