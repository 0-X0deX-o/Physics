class Vector_2D:

    def __init__(self, deg_angle = None, magnitude = None, x_component = None, y_component = None):
        self.deg_angle = deg_angle
        self.magnitude = magnitude
        self.x_component = x_component
        self.y_component = y_component
        self.degrees = True

    def degrees_to_radians(self):
        pass

    def radians_to_degrees(self):
        pass

    def compute_components(self):
        pass

    def compute_magnitude(self):
        pass

    def get_magnitude(self):
        return magnitude

    def get_components(self):
        return x_component, y_component

    def get_angle(self):
        return deg_angle      

    