"""
    \vec{A} has components A_x = -5.00m A_y = 3.00 A_z = 0
    \vec{B} has components B_x = 2.50m B_y = 4.00 B_z = -1.50
    Find the angles between the two vectors
    
"""
from phi_from_scalar_product_dividend_3D import get_scalar_phi
import math

A = [-5.00, 3.00, 0]
B = [2.50, 4.00, -1.50]

def comp_mag_3D(V):
    a = V[0]**2
    b = V[1]**2
    c = V[2]**2
    mag = math.sqrt(a + b + c)
    return mag

A_mag = comp_mag_3D(A)
B_mag = comp_mag_3D(B)
phi = get_scalar_phi(A_mag, B_mag, A, B)
print(f'phi is = to {phi}{chr(176)}')