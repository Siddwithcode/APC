class StudentResult:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks # Expecting a list of 5 subjects

    def calculate_total(self):
        return sum(self.marks)

    def calculate_percentage(self):
        return (self.calculate_total() / 500) * 100

    def calculate_grade(self):
        perc = self.calculate_percentage()
        if perc >= 90:
            return 'A'
        elif perc >= 75:
            return 'B'
        elif perc >= 50:
            return 'C'
        else:
            return 'F'

    def __del__(self):
        print(f"Result processing completed for {self.student_name}.")

result = StudentResult("Charlie", [85, 92, 78, 88, 95])
print(f"Total: {result.calculate_total()}, Percentage: {result.calculate_percentage()}%, Grade: {result.calculate_grade()}")
