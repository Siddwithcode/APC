class Person:
    def display_role(self): pass
class Student(Person):
    def display_role(self): print("I am a Student")
class Faculty(Person):
    def display_role(self): print("I am Faculty")
class Administrator(Person):
    def display_role(self): print("I am an Admin")
for p in [Student(), Faculty(), Administrator()]: p.display_role()
