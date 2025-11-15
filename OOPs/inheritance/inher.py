# Inheritance is simply the mechanism where a new class can inherit the attributes and methods of an existing class.
# we use inheritance to:
# Reuse Code: Avoid rewriting the same attributes and methods in multiple classes.
# Establish Relationships: Create a clear "is-a" relationship (e.g., A Dog is a type of Animal).
# super().__init__(name)- used to call the constructor of parent class in child class.
# Ex:- 

class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        print("Some generic animal sound..!!")

    def show_data(self):
        print("---Details---")
        print("Name:- ",self.name)
        print("Species:- ",self.species)

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name,species='Canine')
        self.breed = breed

    def make_sound(self):
        print(f"{self.name} Says: Woof! Woof!")

    def fetch(self):
        print(f"{self.name}({self.breed}) is running to fetch the ball!")

generic_animal = Animal("Zebra","Equidae")
max_dog = Dog("Max","Golden Retriewer")

generic_animal.show_data()
generic_animal.make_sound()
max_dog.show_data()
max_dog.make_sound()

