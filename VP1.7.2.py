"""
Consider the three vectors \vec{A} \vec{B} and \vec{C}
in Example 1.7. Calculate the magnitude and direction of the vector 
\vec{S} = \vec{A} - \vec{B} + \vec{C}
State the direction of \vec{S} in terms of an angle measured
counterclockwise from the postive x-axis, and state in 
which quadrant this angle lives.


======================================================
Example 1.7
\vec{A} = 72.4m, 32.0\degrees east of north
\vec{B} = 57.3m, 36.0\degrees south of west
\vec{A} = 17.8m, due south
======================================================
"""
# step one create the return reverse of a vector

from vector_addition_2D import vector_addition_2D
from vector_2D import Vector_2D
from reverse_2D_vector_ang_mag import reverse_vector_components
import math

A_ang = 90 - 32  

A = Vector_2D(A_ang, 72.4)
A.compute_components()
A_comp = A.get_components()

B_ang = 180  + 36  
B_neg = reverse_vector_components([B_ang, 57.3])
B = Vector_2D(B_neg[0], B_neg[1])
B.compute_components()
B_comp = B.get_components()


C_ang = 270  
C = Vector_2D(C_ang, 17.8)
C.compute_components()
C_comp = C.get_components()


add_prepped_comp = [A_comp,B_comp,C_comp]
S_comp = vector_addition_2D(add_prepped_comp)
S_comp[0] *= (180/math.pi)
S = Vector_2D(S_comp[0], None, S_comp[1], S_comp[2])
S.compute_magnitude()
S_deliverables = [S.get_angle(), S.get_magnitude()]

print(f'The vector "S": {S_deliverables[0]}{chr(176)} magnitude {S_deliverables[1]}')

# must be in the format of list [degree, magnitude] and returned in the same format

# 1. Find the Resultant Vector (A+B+C)

# (A+B+C) = -D

# should I add units?