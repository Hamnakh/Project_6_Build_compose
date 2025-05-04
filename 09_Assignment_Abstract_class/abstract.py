from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        # Abstract method (must be implemented by subclass)
        pass

# Concrete subclass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        # Implementing the abstract method
        return self.width * self.height


# Trying to create an object of Shape will raise an error
# shape = Shape()  ❌ Not allowed

# Create a Rectangle object
rect = Rectangle(5, 4)

# Display the area
print("Area of Rectangle:", rect.area())
