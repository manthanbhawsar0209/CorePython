class Car:
    NumberOfGears = 6

    def __init__(self):
        self.__colour = None
        self.__speed = None
        self.__model = None

    def set_colour(self, colour):
        self.__colour = colour

    def get_colour(self):
        return self.__colour

    def set_model(self, model):
        self.__model = model

    def get_model(self):
        return self.__model

    def set_speed(self, speed):
        self.__speed = speed

    def get_speed(self):
        return self.__speed

    def brake(self):
        if self.__speed == 0:
            print("Car is stopped")
        else:
            self.__speed = self.__speed - 10
            print("Current speed is", self.__speed)

    def accelerate(self):
        if self.__speed > 200:
            print("You are going very fast, please slow down")
        else:
            self.__speed = self.__speed + 10
            print("Current speed is", self.__speed)

    def GearChange(self, gear):
        if gear > Car.NumberOfGears:
            print("Invalid gear")
        else:
            print("Gear changed to ", gear)
c = Car()
c.set_colour("Black")
c.set_model("Lamborghini")
c.set_speed(100)
print("Car colour:", c.get_colour())
print("Car speed: ", c.get_speed())
print("Car model: ", c.get_model())
c.brake()
c.accelerate()
c.GearChange(5)
