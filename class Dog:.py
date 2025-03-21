class Dog:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    # Make the dog bark
    def bark(self):
        print(f"{self.name} says: Woof, woof!")

    # Method to display the dog's age
    def display_age(self):
        print(f"{self.name} is {self.age} years old")


# Create an instance (object) of the Dog class
dog1 = Dog("Buddy", 3)

# Use the methods of the dog object
dog1.bark()
dog1.display_age()
