"""
Vector \vec{A} has magnitude 5.00
and is at an angle of 36.9 deg south of east
Vector \vec{B} has magnitude 6.40 and is at 
    at an angle of 20.0 deg west of north
    (a). Choose the positive x-direction to
        the east and the positive y-direction
        to the north. Find the components of 
        \vec{A} and \vec{B}.
    (b). Calculate the scalar product \vec{A}\cdot \vec{B} 
"""
from vector_2D import Vector_2D
from vector_product_scalar_2D import scalar_product_2D

A_deg = 360 - 36.9
A = Vector_2D(A_deg, 5.00)
A_comp = A.getcomponents()

B_deg = 90 + 20
B = Vector_2D(B_deg, 6.40)
B_comp = B.getcomponents()

A_mag = A.get_magnitude()
B_mag = B.get_magnitude()
angles = []
angles.append(A.get_angle())
angles.append(B.get_angle())

scalar_product = scalar_product_2D(A_mag, B_mag, angles)

print(f'The components of A are x: {A_comp[0]} and y: {A_comp[1]}')
print(f'The components of B are x: {B_comp[0]} and y: {B_comp[1]}')
print(f'The scalar_product of A and B is {scalar_product}') 