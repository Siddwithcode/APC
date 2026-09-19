class Shape:
    def display_name(self): print(self.__class__.__name__)
class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14 * self.r**2
class Rectangle(Shape):
    def __init__(self, l, w): self.l, self.w = l, w
    def area(self): return self.l * self.w
class Triangle(Shape):
    def __init__(self, b, h): self.b, self.h = b, h
    def area(self): return 0.5 * self.b * self.h
c = Circle(5); c.display_name(); print(c.area())
