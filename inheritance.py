# Base class (Parent)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Derived class (Child)
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

# Another derived class
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

# Create instances
dog = Dog("Buddy")
cat = Cat("Whiskers")
