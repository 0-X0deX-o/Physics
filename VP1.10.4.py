"""
If a force \vec{Facts on an object as that object moves through 
through displacement \vec{s}, the work done by tha force equals 
the scalar project of \vec{F and \vec{s}: W = \cev{F}\cdot \vec{s}.
A certain object moves through displacement 
\vec{s} = (4.00)\hat{i} + (5.00)\hat{j}. As it moves it is acted on by
force \vec{F}, which has x-component F_x = -12.0 N (1 N = 1 newton is
the SI unti of force). The work done by this force is 26.0 N\cdot m = 26.0 J
(1 J = 1 joule = 1 newton-meter is the SI unit of work). 

    a.) Find the y-component of \vec{F}.
    b.) Find the angel between \vec{F} and \vec{s}.
 
Given an equation
find the target variable

    Equation: W = \vec{F}\cdot \vec{s}


"""

from vector_2D import Vector_2D
from vector_product_scalar_2D import get_phi


s = Vector_2D(0,0,4.00, 5.00)
s.compute_magnitude()
s.compute_angle()
s.radians_to_degrees()
s_angle = s.get_angle()

F = Vector_2D(0,0,-12.0, 14.8)
F.compute_magnitude()
F.compute_angle()
F.radians_to_degrees()
F_angle = F.get_angle()

angles = []
angles.append(s.get_angle())
angles.append(180 + F.get_angle())
phi = get_phi(angles)

F_comp = F.get_components()

print(f'The target y-component is {F_comp[1]}')
print(f'The angle phi is {phi}{chr(176)}')