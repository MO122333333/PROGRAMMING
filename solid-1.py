from math import pi
from abc import ABC, abstractmethod


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class ShapePrinter:
    def print_area(self, shape):
        print(f"The area is: {shape.area()}")


def calculate_area(shape: Shape):
    return shape.area()


if __name__ == "__main__":
    
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(3, 7)
    square = Square(4)

    
    printer = ShapePrinter()
    printer.print_area(circle)      
    printer.print_area(rectangle)   
    printer.print_area(triangle)    
    printer.print_area(square)      