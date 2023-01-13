import math

def get_scalar_phi(A_mag, B_mag, A_comp, B_comp):
    sum = 0
    for i in range(len(A_comp)):
        A_comp[i] *= B_comp[i]
        sum += A_comp[i]
    phi = math.acos(sum/(A_mag * B_mag))
    phi *= (180/math.pi)
    return phi