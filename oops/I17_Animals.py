class Animal:
    def __init__(self, name): self.name = name
class Dog(Animal):
    def sound(self): return "Bark"
class Cat(Animal):
    def sound(self): return "Meow"
class Cow(Animal):
    def sound(self): return "Moo"
d = Dog("Buddy")
print(f"{d.name} says {d.sound()}")
