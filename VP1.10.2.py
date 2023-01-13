"""
    Vector \vec{C} has magnitude 6.50 and is at an angle of 55.0 deg pos x-axis
    Vector \vec{D} has components (4.80, -8.40)
    a. calculate the scalar  product \vec{C}\cdot \vec{D}.
    b. Find the angle \phi between the vectors \vec{C} and \vec{D}

"""
from vector_2D import Vector_2D
from vector_product_scalar_2D import scalar_product_2D, get_phi

# TODO: Compute phi and return it

C = Vector_2D(55.0, 5.00)

D = Vector_2D(0,0, 4.80, -8.40)
D.compute_magnitude()
D.compute_angle()
D.radians_to_degrees()

C_mag = C.get_magnitude()
D_mag = D.get_magnitude()
angles = []
angles.append(C.get_angle())
angles.append(D.get_angle())
phi = get_phi(angles)
scalar_product = scalar_product_2D(C_mag, D_mag, angles)

print(f'The scalar_product of C and D is {scalar_product}') 
print(f'The angle phi between the two vectors is {phi}{chr(176)}')