from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def perimeter(self):
        pass
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def volume(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def volume(self):
        # Volume of a sphere (4/3 πr³)
        return (4/3) * math.pi * self.radius ** 3

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def area(self):
        return self.length * self.width
    
    def volume(self, height=None):
        # Volume of a rectangular prism (l × w × h)
        # For 2D rectangle, height would need to be provided
        if height is None:
            return 0
        return self.length * self.width * height

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def perimeter(self):
        return 4 * self.side
    
    def area(self):
        return self.side ** 2
    
    def volume(self, height=None):
        # Volume of a cube or square prism (side³ or side² × height)
        if height is None:
            return self.side ** 3
        return self.side ** 2 * height