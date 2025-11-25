# METHOD OVERLOADING :- 
'''
- Multiple methods with same name but different parameters lists is called as Method Overloading.
- but python doesnot supports Method Overloading.
-  If we defing multiple methods with same class within a single class only the latest will be recognized by the interpreter.
- However python provides several ways to achieve similar functionality and flexibility, allowing a single method to behave differently based on the arguments provided.
- Below is the example of the Keyword variable length Argument.
'''

class Calci:
    def sub(self,a,b):
        print(f"Substraction of 2 numbers:- {a-b}")
    def sub(self,a,b,c):
        print(f"Substraction of 3 numbers: {a-b-c}")
    def sub(self,a,b,c,d):
        print(f"Substraction of 4 numbers:- {a-b-c-d}")

s = Calci()
# s.sub(10,20) # Calci.sub() missing 2 required positional arguments: 'c' and 'd'.
#               (It will produce error bcz it is looking for 4 arguments bcz the last mwthod will accept 4 arguments.)
s.sub(10,20,30,40) # It will produce output bcz the last one will run and the 4 arguments are passed.
#s.sub(10,20,30) # If we give 3 arguments it will produce error.

# This is how we use method Overloading in python if we want to use it.
'''class Calci:
    def add(self,*args):
        if len(args) == 2:
            print(f"Addition of 2 numbers are: {sum(args)}")
        elif len(args) == 3:
            print(f"Addition of 3 numbers are: {sum(args)}")
        elif len(args) == 4:
            print(f"Addition of 4 numbers are: {sum(args)}")
        elif len(args) == 5:
            print(f"Addition of 5 numbers are: {sum(args)}")
        else:
            print(f"Addition is :{sum(args)}")
c = Calci()
c.add(10,20)
c.add(10,20,30)
c.add(10,20,30,40)
c.add(10,20,30,40,50)
c.add(10,20,30,40,50,60,70,80)'''