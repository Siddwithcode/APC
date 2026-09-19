class Shape:
    def area(self): pass
class Circle(Shape):
    def area(self): print("Circle Area: pi*r^2")
class Rectangle(Shape):
    def area(self): print("Rectangle Area: l*w")
class Triangle(Shape):
    def area(self): print("Triangle Area: 0.5*b*h")
for s in [Circle(), Rectangle(), Triangle()]: s.area()
