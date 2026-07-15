class shape:
    def execute(self):
        print("Shape class executed")
        self.area()

    def area(self):
        print("Shape Area")

class rectangle(shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        rectangle_area = self.width * self.length
        print("Rectangle Area: ", rectangle_area)

class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        circle_area = 3.14 * self.radius * self.radius
        print("Circle Area: ", circle_area)

class test(shape):
    pass

r = rectangle(5,10)
c = circle(5)
t = test()
r.execute()
c.execute()
t.execute()