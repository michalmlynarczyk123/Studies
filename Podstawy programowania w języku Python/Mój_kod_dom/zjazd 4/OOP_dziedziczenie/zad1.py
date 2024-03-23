class Shape:
    pass

class Rectangle(Shape):
    pass

class Triangle(Shape):
    pass

class Circle(Shape):
    pass

figures = [Rectangle(), Triangle(), Circle()]

for f in figures:
    print(type(f))