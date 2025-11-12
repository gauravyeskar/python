# Creating Calculator from modules

def add():
    print("Enter the two values for Addition: ")
    a,b = int(input()),int(input())
    c=a+b
    print(f"The sum of {a} and {b} is {c}.")

def sub():
    print("Enter the two values for Substraction: ")
    a,b = int(input()),int(input())
    c = a-b
    print(f"The Substractions of {a} and {b} is {c}.")

def mul():
    print("Enter the two values for multiplication: ")
    a,b = int(input()),int(input())
    c = a*b
    print(f"The Multipication of {a} and {b} is {c}.")

def div():
    print("Enter the two values for division: ")
    a,b = int(input()),int(input())
    c = a/b
    print(f"The Division of {a} and {b} is {c}.")

def floordiv():
    print("Enter the two values for floor division: ")
    a,b = int(input()),int(input())
    c = a//b
    print(f"The Floor Division of {a} and {b} is {c}.")

def mod():
    print("Enter the two values for modulos: ")
    a,b = int(input()),int(input())
    c = a % b
    print(f"The Modulos of {a} and {b} is {c}.")

def expo():
    print("Enter the two values for Exponential Ooperation: ")
    a,b = int(input()),int(input())
    c = a**b
    print(f"The Power of {a} to {b} is {c}.")