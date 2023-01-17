from mpg_kml import mpg_kml

ev_mileage_mpg = 55.0
capacity = 45
distance = 1500

"""
    a. If you are driving this car in 
        Europe and want to compare its 
        mileage with that of other 
        European cars, express this 
        mileage in km/L (L = liter). 
    
    b. If this car's gas tank holds 45L,
        how many tanks of gas will you 
        use to drive 1500 km?
"""

liters_per_kilometer = mpg_kml(ev_mileage_mpg)
kilometers_per_tank = distance / (liters_per_kilometer * capacity)
print(f"The rate of petrol consumption in For the EV in liters per km is {liters_per_kilometer}")
print(f"The amount of petrol tanks needed to complete a journey of 1500 km is {kilometers_per_tank} tanks")