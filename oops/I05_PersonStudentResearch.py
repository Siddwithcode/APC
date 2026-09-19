class Person:
    def __init__(self, name, age): self.name, self.age = name, age
class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no, self.course = roll_no, course
class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, topic, guide):
        super().__init__(name, age, roll_no, course)
        self.topic, self.guide = topic, guide
    def display(self):
        print(f"{self.name}, {self.course}, Topic: {self.topic}, Guide: {self.guide}")
r = ResearchStudent("Dan", 25, 1, "PhD", "AI", "Dr. Smith")
r.display()
