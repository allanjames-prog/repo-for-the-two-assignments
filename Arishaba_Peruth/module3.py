# class Shape that holds general properties of shapes
class Shape:
# Constructor initializes the properties of a shape
    def __init__(self, name, shape, radius, sides, area, perimeter):
        self.name = name
        self.shape = shape
        self.radius = radius
        self.sides = sides
        self.area = area
        self.perimeter = perimeter

# Method to display the details of the shape   
    def details(self):
        print(f"Name: {self.name}, Shape: {self.shape}, Radius: {self.radius}, Sides: {self. sides}, Area: {self.area}, Perimeter: {self.perimeter}")

# Class Circle inherits from Shape class and adds specific functionality
class Circle(Shape):
    def example(self):
        print("Example is Globe")

# Class Square inherits from Circle and also shape and shows the method with an example
class Square(Circle):
    def example(self):
        print("Example is Box")

# Class Triangle inherits from Square  (and thus also Circle and Shape)
class Triangle(Square):
    def example(self):
        print("Example is Triangular Prism")

# Class Rectangle inherits from Triangle (and thus also Square, Circle, and Shape)
class Rectangle(Triangle):
    def example(self):
        print("Example is a door")

# Class Hexagon inherits from Rectangle (and thus also Triangle, Square, Circle, and Shape)
class Hexagon(Rectangle):

# Additional methods for specific Hexagon-related examples
    def example1(self):
        print("Example 1 is paver")

    def example2(self):
        print("Example 2 is Bee hive")

    def example3(self):
        print("Example3 is a Honey Comb")

    def example4(self):
        print("Example4 is a Soccer ball top layer design ")

    def example5(self):
        print("Example5 is snow flakes")

# Creating an instance of Circle and displaying its details and example
circle = Circle("Circle", "Circular", 20, 1, 1257, 125.6)
circle.details()
circle.example()
print("\n......................................................") 

# Creating an instance of Square and displaying its details and example
square = Square("Square", "Angular", 0, 4, 25,  20)
square.details()
square.example()
print("\n......................................................") 

# Creating an instance of Triangle and displaying its details and example
triangle = Triangle("Triangle", "Triangular", 0, 3, 25, 22.7)
triangle.details()
triangle.example()
print("\n......................................................") 

# Creating an instance of Rectangle and displaying its details and example
rectangle = Rectangle("Rectangle", "Rectangular", 0, 4, 21, 20)
rectangle.details()
rectangle.example()
print("\n......................................................") 

# Creating an instance of Hexagon and displaying its details and various example
hexagon = Hexagon("Hexagon", "Hexagonal", 0, 6, 41.57, 24)
hexagon.details()
hexagon.example1()
hexagon.example2()
hexagon.example3()
hexagon.example4()
hexagon.example5()
