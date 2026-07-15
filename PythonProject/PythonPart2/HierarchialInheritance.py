class shape:
    def __init__(self, colour, border_colour):
        self.border_colour = border_colour
        self.colour = colour

    # def set_border(self, border_colour):
    #     self.border_colour = border_colour

    # def set_colour(self, colour):
    #     self.colour = colour

    def get_border(self):
        return self.border_colour

    def get_colour(self):
        return self.colour

class circle(shape):
    def __init__(self, radius, colour, border_colour):
        self.radius = radius
        super().__init__(colour, border_colour)

    # def set_radius(self, radius):
    #     self.radius = radius

    def get_radius(self):
        return self.radius

class rectangle(shape):
    def __init__(self, length, width, colour, border_colour):
        self.length = length
        self.width = width
        super().__init__(colour, border_colour)

    # def set_length(self, length):
    #     self.length = length

    def get_length(self):
        return self.length

    # def set_width(self, width):
    #     self.width = width

    def get_width(self):
        return self.width

r = rectangle(10, 5, "red", "black")
c = circle(10, "blue", "black")
print("Rectangle:")
print("Length:", r.get_length())
print("Width:", r.get_width())
print("Colour:", r.get_colour())
print("Border Colour:", r.get_border())
print("Circle:")
print("Radius:", c.get_radius())
print("Colour:", c.get_colour())
print("Border Colour:", c.get_border())
