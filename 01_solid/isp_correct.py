# Interface segregation Principle - Correct
from abc import ABC, abstractmethod


class TwoDShape(ABC):
    def __init__(self, length, breath):
        self.length = length
        self.breath = breath

    @abstractmethod
    def area(self):
        pass


class ThreeDShape(TwoDShape):
    def __init__(self, length, breath, height):
        super().__init__(length, breath)
        self.height = height

    @abstractmethod
    def volume(self):
        pass


class Rectangle(TwoDShape):
    def __init__(self, length, breath):
        super().__init__(length, breath)

    def area(self):
        area = self.length * self.breath
        return f"Area of rectangle is {area}"


class Cuboid(ThreeDShape):
    def __init__(self, length, breath, height):
        super().__init__(length, breath, height)

    def area(self):
        area = 2 * self.height * (self.length + self.breath)
        return f"Area of rectangle is {area}"

    def volume(self):
        volume = self.length * self.breath * self.height
        return f"Volume of rectangle is {volume}"


rec = Rectangle(3, 5)
print(rec.area())

cuboid = Cuboid(2, 3, 4)
print(cuboid.area())
print(cuboid.volume())
