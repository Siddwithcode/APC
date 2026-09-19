class Student:
    def __init__(self, roll, name, course):
        self.roll, self.name, self.course = roll, name, course
class Result(Student):
    def __init__(self, roll, name, course, m1, m2, m3):
        super().__init__(roll, name, course)
        self.marks = [m1, m2, m3]
    def calculate(self):
        tot = sum(self.marks)
        perc = tot / 3
        grade = "A" if perc > 80 else "B"
        print(f"Total: {tot}, Perc: {perc:.2f}%, Grade: {grade}")
r = Result(1, "Ana", "CS", 85, 90, 88)
r.calculate()
