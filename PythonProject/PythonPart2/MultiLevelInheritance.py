class outline:
    def __init__(self):
        self.borderwidth = None

    def set_borderwidth(self, bw):
        self.borderwidth = bw

    def get_borderwidth(self):
        return self.borderwidth

class shape(outline):
    def __init__(self):
        self.colour = None
        self.border_colour = None

    def set_colour(self, c):
        self.colour = c

    def get_colour(self):
        return self.colour

    def set_border_colour(self, b):
        self.border_colour = b

    def get_border_colour(self):
        return self.border_colour

class rectangle(shape):
    def __init__(self):
        self.length = None
        self.width = None

    def set_length(self, l):
        self.length = l

    def set_width(self, w):
        self.width = w

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width

r = rectangle()
r.set_length(5)
r.set_width(3)
r.set_colour("red")
r.set_border_colour("black")
r.set_borderwidth(100)
print("Length:", r.get_length())
print("Width:", r.get_width())
print("Colour:", r.get_colour())
print("Border Colour:", r.get_border_colour())
print("Border Width: ", r.get_borderwidth())
