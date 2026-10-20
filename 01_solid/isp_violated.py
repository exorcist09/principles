# Interface segregation Principle - Violated
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, length, breath, height):
        self.length = length
        self.breath = breath
        self.height = height

    @abstractmethod    
    def area(self):
        pass

    @abstractmethod
    def volume(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, breath):
        super().__init__(length, breath, 0)

    def area(self):
        super().area()
        area = self.length * self.breath
        return f"Area of rectangle is {area}"
    

class Cuboid(Shape):
    def __init__(self, length, breath, height):
        super().__init__(length, breath, height)

    def area(self):
        super().area()
        area = 2 * self.height*(self.length + self.breath)
        return f"Area of rectangle is {area}"

    def volume(self):
        super().volume()
        volume = self.length * self.breath * self.height
        return f"Volume of rectangle is {volume}"


rec = Rectangle(3,5)
print(rec.area())
print(rec.volume())

cuboid = Cuboid(2,3,4)
print(cuboid.area())
print(cuboid.volume())
