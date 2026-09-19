class Person:
    def __init__(self, name): self.name = name
class Student(Person): pass
class Faculty(Person): pass
class TeachingAssistant(Student, Faculty):
    def __init__(self, name): super().__init__(name)
    def display(self): print(f"TA: {self.name}")
t = TeachingAssistant("Tom")
t.display()
