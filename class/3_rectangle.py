class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth

    def calculate_perimeter(self):
        return 2 * (self.length + self.breadth)

rect = Rectangle(10, 5)
print(f"Area: {rect.calculate_area()}, Perimeter: {rect.calculate_perimeter()}")
