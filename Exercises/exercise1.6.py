"""
    1.6 The following conversions occur frequently in physics and are very useful.
    (a) Use 1 mi = 5280 ft and 1 h = 3600 s to convert 60 mph to units of ft/s.
    (b) The acceleration of a freely falling object is 32 ft/s^2.
        Use 1 ft. = 30.48 cm to express this acceleration in units of m/s^2
    (c) The density of water is 1.0g/cm^3. Convert this density to units of kg/m^3.
"""

def mph_to_fps(mph):
    return mph * (5280/3600)

def entrance_menu():
    print("This program takes an integer for mph speed from user input and returns a conversion to units fps: ")
    speed_mph = int(input("Enter what speed you want to convert: "))
    return speed_mph

speed_mph = entrance_menu()
speed_fps = mph_to_fps(speed_mph)
print(speed_fps)