"""
    In the fall of 2002, scientists at Los Alamos National Laboratory
    determined that the critical mass of neptunium-237 is about 60kg. 
    The critical mass of a fissionable material is the minimum amount
    that must be brought together to start a nuclear chain reaction.
    Neptunimum-237 has a density of 19.5 g/cm^3.
    What would be the radius of a sphere of this material that has a critical mass?
"""
import math


critical_mass_kg = 60
rho_kg_cm_cubed = 19.5e-3
radius = math.pow(((4*60)/(3*rho_kg_cm_cubed*math.pi)), (1/3))

print(f'The radius of a sphere whose density is {rho_kg_cm_cubed} kg/cm^3 and mass is 60 kg is {"{:.2f}".format(radius)} cm')