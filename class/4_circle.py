import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

    def calculate_circumference(self):
        return 2 * math.pi * self.radius

circle = Circle(7)
print(f"Area: {circle.calculate_area():.2f}, Circumference: {circle.calculate_circumference():.2f}")
