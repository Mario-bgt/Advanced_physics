from geometric_object import GeometricObject
pi = 3.14


class Cylinder(GeometricObject):
    def __init__(self, radius, height, color, filled):
        super().__init__(color, filled)
        self.radius = radius
        self.height = height

    def area(self):
        return round(2*pi*self.radius*(self.radius+self.height),2)

    def volume(self):
        return round(pi*self.radius**2*self.height,2)
