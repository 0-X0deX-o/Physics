"""
    type: List[List]
    rtype: [list]
"""
# returns angles in radians
import math

def vector_addition_2D(vectors):
    for i in range(len(vectors[0])): 
        for j in range(1,len(vectors)):
            vectors[0][i] += vectors[j][i]
    vectors[0].insert(0,math.atan(vectors[0][1]/vectors[0][0]))
    vectors = vectors[0]
    return vectors