import math

class Vector_2D:

    def __init__(self, deg_angle = None, magnitude = None, x_component = None, y_component = None):
        self.deg_angle = deg_angle
        self.magnitude = magnitude
        self.x_component = x_component
        self.y_component = y_component
        self.degrees = True

    def degrees_to_radians(self):
        if self.degrees == True:
            self.deg_angle *= (math.pi/180)
            self.degrees = False

    def radians_to_degrees(self):
        if self.degrees == False:
            self.deg_angle *= (180/math.pi)
            self.degrees = True

    # verify answers when computing angles
    def compute_angle(self):
        if self.x_component != None and self.y_component != None:
            self.degrees = False
            self.deg_angle = math.atan(self.y_component/self.x_component)


    def compute_components(self):
        if self.deg_angle != None and self.magnitude != None:
            if self.degrees == True:
                self.x_component = self.magnitude * math.cos(self.deg_angle * (math.pi/180))
                self.y_component = self.magnitude * math.sin(self.deg_angle * (math.pi/180))
            elif self.degrees == False:
                self.x_component = self.magnitude * math.cos(self.deg_angle)
                self.y_component = self.magnitude * math.sin(self.deg_angle)

    def compute_magnitude(self):
        if self.x_component != None and self.y_component != None:
            a = self.x_component**2
            b = self.y_component**2
            c = a + b
            c **= .5
            self.magnitude = c

    def set_degrees(self, boolean = True):
        self.degrees = boolean

    def get_magnitude(self):
        return self.magnitude

    def get_components(self):
        return [self.x_component, self.y_component]

    def get_angle(self):
        return self.deg_angle