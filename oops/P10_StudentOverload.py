class Student:
    def __init__(self, name, marks): self.name, self.marks = name, marks
    def __gt__(self, other): return self.marks > other.marks
    def __lt__(self, other): return self.marks < other.marks
s1 = Student("A", 80)
s2 = Student("B", 90)
print("S2 > S1:", s2 > s1)
