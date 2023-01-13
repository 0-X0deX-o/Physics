"""
Consider the three vectors A B and C in example 1.7
If a fourth vector D is add to A + B + C, the result is zero:
A+B+C+D=0. Find the magnitude and direction of D.
State the direction of D in terms of an angle measured counterclockwise from...
the positive x-axis and state in which quadrant this angle lies.

======================================================
Example 1.7
\vec{A} = 72.4m, 32.0\degrees east of north
\vec{B} = 57.3m, 36.0\degrees south of west
\vec{A} = 17.8m, due south
======================================================
"""
from vector_addition_2D import vector_addition_2D
from vector_2D import Vector_2D

A_ang = 90 - 32  
A = Vector_2D(A_ang, 72.4)
A.compute_components()
A_comp = A.get_components()

B_ang = 180  + 36  
B = Vector_2D(B_ang, 57.3)
B.compute_components()
B_comp = B.get_components()

C_ang = 270  
C = Vector_2D(C_ang, 17.8)
C.compute_components()
C_comp = C.get_components()


add_prepped_comp = [A_comp,B_comp,C_comp]
resultant = vector_addition_2D(add_prepped_comp)
print(resultant)
# 1. Find the Resultant Vector (A+B+C)

# (A+B+C) = -D

# should I add units?