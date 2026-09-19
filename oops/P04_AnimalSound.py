class Animal:
    def sound(self): pass
class Dog(Animal):
    def sound(self): print("Bark")
class Cat(Animal):
    def sound(self): print("Meow")
class Cow(Animal):
    def sound(self): print("Moo")
class Lion(Animal):
    def sound(self): print("Roar")
for a in [Dog(), Cat(), Cow(), Lion()]: a.sound()
