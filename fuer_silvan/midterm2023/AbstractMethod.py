from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

# Attempt to create an instance of the abstract class (Shape) will raise an error
# shape = Shape()  # This will raise a TypeError

# Create instances of concrete subclasses (Circle and Square)
circle = Circle(5)
square = Square(4)

# Call the area method for each shape
print("Circle Area:", circle.area())  # Output: "Circle Area: 78.5"
print("Square Area:", square.area())  # Output: "Square Area: 16"