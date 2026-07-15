from abc import ABC, abstractmethod

class shape(ABC):
    def execute(self):
        print("Executing shape")
        self.area()

    @abstractmethod
    def area(self):
        pass

class Rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        print("Area is", area)

r = Rectangle(10,20)
#s = shape()
r.execute()
s : shape = Rectangle(5,5)
s.execute()

