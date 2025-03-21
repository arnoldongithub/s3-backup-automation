class Animal:
       def __init__(self, name, species):
              self.name=name
              self.species=species
       def make_sound(self):
              pass
#child class(derived class)
       def __init__(self, name, breed):
              #call the init
               super().__init__(name, species="Dog")
               self.breed=breed
       def make_sound(self):
              return "woof"
#child class (derived class)
class Cat(Animal):
       def __init__(self, name, breed):
              #call the init method of the parent class using super()
              super().__init__(name, species='Dog')
              self.breed=breed
       def make_sound(self):
              return "Woof!"
class Cat(Animal):
       def __init__(self, name, breed):
              #call the init method of the parent class using super()
              super().__init__(name, species='cat')
              self.breed=breed
       def make_sound(self):
              return "Meow!"
#creating instances of child classes
dog_instance=Dog("Buddy","Golden Retriever")
cat_instance=Cat("whiskers","siamese")

#accessing properties and methods of the parent and child classes
print (f"{dog_instance.name} is a {dog_species} of breed (dog_instance.breed)")
print (f"dog_instance.name) says: {dog_instance.make_sound()}")

print (f"{cat_instance.name} is a {cat_instance.species} of breed {cat_instance.breed}.")
print (f"{cat_instance.name} says: {cat_instance.make_sound( ) }")
