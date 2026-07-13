class shape:
    def __init__(self, colour, border_colour):
        self.colour = colour
        self.border_colour = border_colour

    def get_colour(self):
        return self.colour

    def get_border_colour(self):
        return self.border_colour

s = shape("red", "black")
print("Colour:", s.get_colour())
print("Border Colour:", s.get_border_colour())