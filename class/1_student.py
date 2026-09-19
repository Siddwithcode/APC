class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display_details(self):
        print(f"Roll No: {self.roll_no}, Name: {self.name}")

    def calculate_percentage(self):
        total = sum(self.marks)
        percentage = (total / (len(self.marks) * 100)) * 100
        print(f"Percentage: {percentage:.2f}%")

# Create multiple students
s1 = Student(1, "Alice", [85, 90, 88])
s2 = Student(2, "Bob", [78, 82, 80])

s1.display_details()
s1.calculate_percentage()
s2.display_details()
s2.calculate_percentage()
