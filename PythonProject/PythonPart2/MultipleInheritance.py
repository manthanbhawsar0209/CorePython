class shape:
    def __init__(self, No_of_lines):
        self.no_of_lines = No_of_lines

    def get_no_of_lines(self):
        return self.no_of_lines

class shape_colour:
    def __init__(self, colour):
        self.colour = colour

    def get_colour(self):
        return self.colour

class rectangle(shape,shape_colour):
    def __init__(self, length, width, No_of_lines, colour):
        self.length = length
        self.width = width
        super().__init__(No_of_lines)
        super().__init__(colour)

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width

r = rectangle(10, 5, 4, "red")
print("length: ", r.get_length())
print("width: ", r.get_width())
print("colour: ", r.get_colour())
print("no_of_lines: ", r.get_no_of_lines())