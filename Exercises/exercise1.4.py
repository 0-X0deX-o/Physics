"""
    the density of gold is 19.3 g/cm**3. 
    What is this value in kilograms per cubic meter?
"""

gold_density_g_cm = 19.3

def g_cm_to_kg_m(density):
    density /= 1000
    density *= 100**3
    return density


density = g_cm_to_kg_m(gold_density_g_cm)
print(f'{density:,} kg/m\N{SUPERSCRIPT THREE}')