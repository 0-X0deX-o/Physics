import math

def scalar_product_2D(A_mag, B_mag, angles):
    for angle in angles:
        if angle < 0:
            angle += 360
    angles.sort()
    phi = angles[1] - angles[0]
    if phi > 180:
        phi = 360 - phi
    phi *= (math.pi/180)
    product = A_mag * B_mag * math.cos(phi)    
    return product

def scalar_product_components_2D(A_comp, B_comp):
    sum = 0
    for i in range(len(A_comp)):
        A_comp[i] *= B_comp[i]
        sum += A_comp[i]
    return sum


def get_phi(angles):
    for angle in angles:
        if angle < 0:
            angle += 360
    angles.sort()
    phi = angles[1] - angles[0]
    if phi > 180:
        phi = 360 - phi
    
    return phi