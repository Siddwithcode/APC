class Academic:
    def __init__(self, marks): self.marks = marks
class Sports:
    def __init__(self, points): self.points = points
class Student(Academic, Sports):
    def __init__(self, name, marks, points):
        Academic.__init__(self, marks)
        Sports.__init__(self, points)
        self.name = name
    def overall_performance(self):
        return self.marks + (self.points * 2)
s = Student("Bob", 85, 5)
print(f"{s.name} Overall: {s.overall_performance()}")
