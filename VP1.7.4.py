"""
A hiker undergoes the displacement \vec{A shown in Example 1.7
The hiker then undergoes a second displacement such that she
ends up 38.0 m from her starting point, in a direction from
her starting point that is 37.0 degrees west of north. Find
the magnitude and direction of this second displacement. State
the direction in terms of an angle measured counterclockwise 
from the positive x-axis, and state in which quadrant this angle lies.

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

A_ang = (90 - 32) + 180
A = Vector_2D(A_ang, 72.4)
A.compute_components()
A_comp = A.get_components()

B_ang = 90 + 37  
B = Vector_2D(B_ang, 38)
B.compute_components()
B_comp = B.get_components()


add_prepped_comp = [A_comp,B_comp]
print(add_prepped_comp)
C_comp = vector_addition_2D(add_prepped_comp)
print(C_comp)
C_comp[0] *= (180/math.pi)
print(C_comp[0])
C = Vector_2D(C_comp[0], None, C_comp[1], C_comp[2])
C.compute_magnitude()

print(f"The vector 'C' is magnitude {C.get_magnitude()} and the angle is {C.get_angle() + 180}{chr(176)}")

# must be in the format of list [degree, magnitude] and returned in the same format

# 1. Find the Resultant Vector (A+B+C)

# (A+B+C) = -D

# should I add units?